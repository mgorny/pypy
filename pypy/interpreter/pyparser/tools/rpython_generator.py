#!/usr/bin/env pypy3

# generate rpython code from pegen grammars. Forked version of
# python_generator.py

import ast
import re
import token
import os

from typing import IO, Any, Dict, Optional, Sequence, Set, Text, Tuple
from pegen import grammar
from pegen.grammar import (
    Alt,
    Cut,
    Forced,
    Gather,
    GrammarVisitor,
    Group,
    Lookahead,
    NamedItem,
    NameLeaf,
    NegativeLookahead,
    Opt,
    PositiveLookahead,
    Repeat0,
    Repeat1,
    Rhs,
    Rule,
    StringLeaf,
)
from pegen.parser_generator import ParserGenerator
from importlib.machinery import SourceFileLoader

here = os.path.dirname(__file__)
pytokenfile = os.path.join(here, "..", "pytoken.py")

pytoken = SourceFileLoader('pytoken', pytokenfile).load_module()


MODULE_PREFIX = """\
#!/usr/bin/env python
# @generated by pegen from {filename}

# Special RPython version

import sys

"""
MODULE_SUFFIX = """

"""


class InvalidNodeVisitor(GrammarVisitor):
    def visit_NameLeaf(self, node: NameLeaf) -> bool:
        name = node.value
        return name.startswith("invalid")

    def visit_StringLeaf(self, node: StringLeaf) -> bool:
        return False

    def visit_NamedItem(self, node: NamedItem) -> bool:
        return self.visit(node.item)

    def visit_Rhs(self, node: Rhs) -> bool:
        return any(self.visit(alt) for alt in node.alts)

    def visit_Alt(self, node: Alt) -> bool:
        return any(self.visit(item) for item in node.items)

    def lookahead_call_helper(self, node: Lookahead) -> bool:
        return self.visit(node.node)

    def visit_PositiveLookahead(self, node: PositiveLookahead) -> bool:
        return self.lookahead_call_helper(node)

    def visit_NegativeLookahead(self, node: NegativeLookahead) -> bool:
        return self.lookahead_call_helper(node)

    def visit_Opt(self, node: Opt) -> bool:
        return self.visit(node.node)

    def visit_Repeat(self, node: Repeat0) -> Tuple[str, str]:
        return self.visit(node.node)

    def visit_Gather(self, node: Gather) -> Tuple[str, str]:
        return self.visit(node.node)

    def visit_Group(self, node: Group) -> bool:
        return self.visit(node.rhs)

    def visit_Cut(self, node: Cut) -> bool:
        return False

    def visit_Forced(self, node: Forced) -> bool:
        return self.visit(node.node)


class PythonCallMakerVisitor(GrammarVisitor):
    def __init__(self, parser_generator: ParserGenerator):
        self.gen = parser_generator
        self.cache: Dict[Any, Any] = {}
        self.keywords: Set[str] = set()
        self.keyword_indices = {}
        self.soft_keywords: Set[str] = set()

    def visit_NameLeaf(self, node: NameLeaf) -> Tuple[Optional[str], str]:
        import pytoken
        name = node.value
        if name == "SOFT_KEYWORD":
            return "soft_keyword", "self.soft_keyword()"
        if name in ("NAME", "NUMBER", "STRING", "OP", "TYPE_COMMENT"):
            name = name.lower()
            return name, f"self.{name}()"
        if name in ("NEWLINE", "DEDENT", "INDENT", "ENDMARKER", "ASYNC", "AWAIT"):
            # pre-lookup the correct type
            if name in pytoken.python_tokens:
                type = pytoken.python_tokens[name]
                call = f"self.expect_type({type!r})"
            else:
                call = f"self.expect({name!r})"
            # Avoid using names that can be Python keywords
            return "_" + name.lower(), call
        return name, f"self.{name}()"

    def visit_StringLeaf(self, node: StringLeaf) -> Tuple[str, str]:
        import pytoken
        val = ast.literal_eval(node.value)
        call = f"self.expect({node.value})"
        if re.match(r"[a-zA-Z_]\w*\Z", val):  # This is a keyword
            if node.value.endswith("'"):
                kw = node.value.strip("'")
                index = self.keyword_indices.setdefault(kw, len(self.keyword_indices) + 499)
                call = f"self.expect_type({index!r})"
                self.keywords.add(val)
            else:
                self.soft_keywords.add(val)
        else:
            op = node.value.strip("'")
            if op in pytoken.python_opmap:
                type = pytoken.python_opmap[op]
                call = f"self.expect_type({type!r})"
        return "literal", call

    def visit_Rhs(self, node: Rhs) -> Tuple[Optional[str], str]:
        if node in self.cache:
            return self.cache[node]
        if len(node.alts) == 1 and len(node.alts[0].items) == 1:
            self.cache[node] = self.visit(node.alts[0].items[0])
        else:
            name = self.gen.name_node(node)
            self.cache[node] = name, f"self.{name}()"
        return self.cache[node]

    def visit_NamedItem(self, node: NamedItem) -> Tuple[Optional[str], str]:
        name, call = self.visit(node.item)
        if node.name:
            name = node.name
        return name, call

    def lookahead_call_helper(self, node: Lookahead) -> Tuple[str, str]:
        name, call = self.visit(node.node)
        head, tail = call.split("(", 1)
        assert tail[-1] == ")"
        tail = tail[:-1]
        # need to hack a bit
        assert head.startswith("self.")
        clsname = self.gen.grammar.metas["class"]
        head = head.replace("self.", clsname + ".")
        return head, tail

    def visit_PositiveLookahead(self, node: PositiveLookahead) -> Tuple[None, str]:
        head, tail = self.lookahead_call_helper(node)
        return None, f"self.positive_lookahead({head}, {tail})"

    def visit_NegativeLookahead(self, node: NegativeLookahead) -> Tuple[None, str]:
        head, tail = self.lookahead_call_helper(node)
        return None, f"self.negative_lookahead({head}, {tail})"

    def visit_Opt(self, node: Opt) -> Tuple[str, str]:
        name, call = self.visit(node.node)
        # Note trailing comma (the call may already have one comma
        # at the end, for example when rules have both repeat0 and optional
        # markers, e.g: [rule*])
        if call.endswith(","):
            return "opt", call
        else:
            return "opt", f"{call},"

    def visit_Repeat0(self, node: Repeat0) -> Tuple[str, str]:
        if node in self.cache:
            return self.cache[node]
        name = self.gen.name_loop(node.node, False)
        self.cache[node] = name, f"self.{name}(),"  # Also a trailing comma!
        return self.cache[node]

    def visit_Repeat1(self, node: Repeat1) -> Tuple[str, str]:
        if node in self.cache:
            return self.cache[node]
        name = self.gen.name_loop(node.node, True)
        self.cache[node] = name, f"self.{name}()"  # But no trailing comma here!
        return self.cache[node]

    def visit_Gather(self, node: Gather) -> Tuple[str, str]:
        if node in self.cache:
            return self.cache[node]
        name = self.gen.name_gather(node)
        self.cache[node] = name, f"self.{name}()"  # No trailing comma here either!
        return self.cache[node]

    def visit_Group(self, node: Group) -> Tuple[Optional[str], str]:
        return self.visit(node.rhs)

    def visit_Cut(self, node: Cut) -> Tuple[str, str]:
        return "cut", "True"

    def visit_Forced(self, node: Forced) -> Tuple[str, str]:
        import pytoken
        name, call = self.visit(node.node)
        if isinstance(node.node, Group):
            return name, f"self.expect_forced({call}, '''({node.node.rhs!s})''')"
        else:
            return (
                name,
                f"self.expect_forced({call}, {node.node.value!r})",
            )


class RPythonParserGenerator(ParserGenerator, GrammarVisitor):
    def __init__(
        self,
        grammar: grammar.Grammar,
        file: Optional[IO[Text]],
        tokens: Set[str] = set(token.tok_name.values()),
        location_formatting: Optional[str] = None,
    ):
        tokens.add("SOFT_KEYWORD")
        super().__init__(grammar, tokens, file)
        self.callmakervisitor: PythonCallMakerVisitor = PythonCallMakerVisitor(self)
        self.invalidvisitor: InvalidNodeVisitor = InvalidNodeVisitor()
        self.unreachable_formatting = "None  # pragma: no cover"
        self.location_formatting = (
            location_formatting
            or "lineno=start_lineno, col_offset=start_col_offset, "
            "end_lineno=end_lineno, end_col_offset=end_col_offset"
        )

    def generate(self, filename: str) -> None:
        header = self.grammar.metas.get("header", MODULE_PREFIX)
        if header is not None:
            self.print(header.rstrip("\n").format(filename=os.path.basename(filename)))
        subheader = self.grammar.metas.get("subheader", "")
        if subheader:
            self.print(subheader)
        cls_name = self.grammar.metas.get("class", "GeneratedParser")
        self.print("# Keywords and soft keywords are listed at the end of the parser definition.")
        self.print(f"class {cls_name}(Parser):")
        while self.todo:
            for rulename, rule in list(self.todo.items()):
                del self.todo[rulename]
                self.print()
                with self.indent():
                    self.visit(rule)

        self.print()
        with self.indent():
            self.print(f"KEYWORD_INDICES = {self.callmakervisitor.keyword_indices}")
            self.print(f"KEYWORDS = {tuple(sorted(self.callmakervisitor.keywords))}")
            self.print(f"SOFT_KEYWORDS = {tuple(sorted(self.callmakervisitor.soft_keywords))}")

        trailer = self.grammar.metas.get("trailer", MODULE_SUFFIX.format(class_name=cls_name))
        if trailer is not None:
            self.print(trailer.rstrip("\n"))

    def alts_uses_locations(self, alts: Sequence[Alt]) -> bool:
        for alt in alts:
            if alt.action and "LOCATIONS" in alt.action:
                return True
            for n in alt.items:
                if isinstance(n.item, Group) and self.alts_uses_locations(n.item.rhs.alts):
                    return True
        return False

    def visit_Rule(self, node: Rule) -> None:
        is_loop = node.is_loop()
        is_gather = node.is_gather()
        rhs = node.flatten()
        if node.left_recursive:
            if node.leader:
                self.print("@memoize_left_rec")
        elif node.memo:
            self.print("@memoize")
        node_type = node.type or "Any"
        self.method_name = node.name
        self.print(f"def {node.name}(self): # type Optional[{node_type}]")
        with self.indent():
            self.print(f"# {node.name}: {rhs}")
            if node.nullable:
                self.print(f"# nullable={node.nullable}")
            self.print("mark = self._index")
            self.print(f"if self._verbose: log_start(self, {node.name!r})")
            if self.alts_uses_locations(node.rhs.alts):
                self.print("tok = self.peek()")
                self.print("start_lineno, start_col_offset = tok.lineno, tok.column")
            if is_loop:
                self.print("children = []")
            self.visit(rhs, is_loop=is_loop, is_gather=is_gather)
            if is_loop:
                self.print("return children")
            else:
                self.print("return None")

    def visit_NamedItem(self, node: NamedItem) -> None:
        name, call = self.callmakervisitor.visit(node.item)
        if node.name:
            name = node.name
        if not name:
            self.print(call)
        else:
            if name != "cut":
                name = self.dedupe(name)
            self.print(f"({name} := {call})")

    def visit_Rhs(self, node: Rhs, is_loop: bool = False, is_gather: bool = False) -> None:
        if is_loop:
            assert len(node.alts) == 1
        for alt in node.alts:
            self.visit(alt, is_loop=is_loop, is_gather=is_gather)

    def named_item_hack(self, node: NamedItem) -> None:
        name, call = self.callmakervisitor.visit(node.item)
        if node.name:
            name = node.name
        if not name:
            return '', call
        else:
            if name != "cut":
                name = self.dedupe(name)
            return f"{name} = {call}", name

    def visit_Alt(self, node: Alt, is_loop: bool, is_gather: bool) -> None:
        invalid = False
        if len(node.items) == 1 and str(node.items[0]).startswith('invalid_'):
            self.print("if self.call_invalid_rules:")
            self.level += 1
            invalid = True
        has_cut = any(isinstance(item.item, Cut) for item in node.items)
        with self.local_variable_context():
            if has_cut:
                self.print("cut = False")

            exprs, assignments = [], []
            for item in node.items:
                assert isinstance(item, NamedItem)
                assignment, expr = self.named_item_hack(item)
                assignments.append(assignment)
                if is_gather:
                    expr += " is not None"
                exprs.append(expr)

            old_level = self.level
            if is_loop:
                self.print("while True:")
                with self.indent():
                    for assignment, expr in zip(assignments, exprs):
                        if assignment.endswith(','): # Optional Rule
                            self.print(assignment.rstrip(','))
                        else:
                            if assignment:
                                self.print(assignment)
                            self.print("if not " + expr + ":")
                            with self.indent():
                                self.print("break")
            else:
                for assignment, expr in zip(assignments, exprs):
                    if assignment.endswith(','): # Optional Rule
                        self.print(assignment.rstrip(','))
                    else:
                        if assignment:
                            self.print(assignment)
                        if assignment != "cut = True":
                            self.print("if " + expr + ":")
                            self.level += 1
                self.level -= 1

            with self.indent():
                action = node.action
                if not action:
                    if is_gather:
                        assert len(self.local_variable_names) == 2
                        action = (
                            f"[{self.local_variable_names[0]}] + {self.local_variable_names[1]}"
                        )
                    else:
                        if self.invalidvisitor.visit(node):
                            action = "UNREACHABLE"
                        elif len(self.local_variable_names) == 1:
                            action = f"{self.local_variable_names[0]}"
                        else:
                            action = f"self.dummy_name()" # {', '.join(self.local_variable_names)})"
                elif "LOCATIONS" in action:
                    self.print("tok = self.get_last_non_whitespace_token()")
                    self.print("end_lineno, end_col_offset = tok.end_lineno, tok.end_column")
                    action = action.replace("LOCATIONS", self.location_formatting)

                if is_loop:
                    self.print(f"children.append({action})")
                    self.print(f"mark = self._index")
                else:
                    if "UNREACHABLE" in action:
                        action = action.replace("UNREACHABLE", self.unreachable_formatting)
                        self.print("assert 0, 'unreachable'")
                    else:
                        self.print(f"return {action}")

            self.level = old_level
            self.print("self._index = mark") # XXX verbose
            # Skip remaining alternatives if a cut was reached.
            if has_cut:
                self.print("if cut: return None")

        if invalid:
            self.level -= 1

def main():
    from sys import argv
    import tokenize
    from pegen.grammar_parser import GeneratedParser as GrammarParser
    from pegen.tokenizer import Tokenizer
    if len(argv) == 3:
        grammar_file, out_file = argv[1:]
    elif len(argv) == 1:
        print("Assuming default values of python-in-rpython.gram and rpypegparse.py")
        grammar_file = os.path.join(here, "python-in-rpython.gram")
        out_file = os.path.join(here, "..", "rpypegparse.py")
    else:
        assert 0, "invalid arguments"
    with open(grammar_file) as file:
        tokenizer = Tokenizer(tokenize.generate_tokens(file.readline))
        parser = GrammarParser(tokenizer)
        grammar = parser.start()

        if not grammar:
            raise parser.make_syntax_error(grammar_file)
    with open(out_file, "w") as file:
        gen = RPythonParserGenerator(grammar, file)
        gen.generate(grammar_file)
    print(grammar)

if __name__ == '__main__':
    main()
