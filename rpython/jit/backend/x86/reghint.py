from rpython.jit.codewriter.effectinfo import EffectInfo
from rpython.jit.metainterp.resoperation import rop
from rpython.jit.metainterp.history import (Const, ConstInt, ConstPtr,
    ConstFloat, INT, REF, FLOAT, VECTOR, TargetToken, AbstractFailDescr)
from rpython.jit.backend.llsupport.descr import CallDescr
from rpython.jit.backend.x86.regloc import (FrameLoc, RegLoc, ConstFloatLoc,
    FloatImmedLoc, ImmedLoc, imm, imm0, imm1, ecx, eax, edx, ebx, esi, edi,
    ebp, r8, r9, r10, r11, r12, r13, r14, r15, xmm0, xmm1, xmm2, xmm3, xmm4,
    xmm5, xmm6, xmm7, xmm8, xmm9, xmm10, xmm11, xmm12, xmm13, xmm14,
    X86_64_SCRATCH_REG, X86_64_XMM_SCRATCH_REG,)
from rpython.jit.backend.x86 import rx86


from rpython.jit.backend.x86.regalloc import (
    X86_64_RegisterManager, X86_64_XMMRegisterManager)

# tell the register allocator hints about which variables should be placed in
# what registers (those are just hints, the register allocator will try its
# best to achieve that).


class X86RegisterHints(object):
    def add_hints(self, longevity, inputargs, operations):
        self.longevity = longevity
        for i in range(len(operations)):
            op = operations[i]
            if rop.has_no_side_effect(op.opnum) and op not in self.longevity:
                continue
            oplist[op.getopnum()](self, op, i)

    def not_implemented_op(self, op, position):
        # no hint by default
        pass


    def consider_int_neg(self, op, position):
        self.longevity.try_use_same_register(op.getarg(0), op)
    consider_int_invert = consider_int_neg

    def _consider_binop_part(self, op, position, symm=False):
        x = op.getarg(0)
        y = op.getarg(1)

        # For symmetrical operations, if y won't be used after the current
        # operation finishes, but x will be, then swap the role of 'x' and 'y'
        if symm:
            if isinstance(x, Const):
                x, y = y, x
            elif (not isinstance(y, Const) and
                    self.longevity[x].last_usage > position and
                    self.longevity[y].last_usage == position):
                x, y = y, x

        if not isinstance(x, Const):
            self.longevity.try_use_same_register(x, op)

    def _consider_binop(self, op, position):
        self._consider_binop_part(op, position)

    def _consider_binop_symm(self, op, position):
        self._consider_binop_part(op, position, symm=True)

    consider_int_mul = _consider_binop_symm
    consider_int_and = _consider_binop_symm
    consider_int_or  = _consider_binop_symm
    consider_int_xor = _consider_binop_symm

    consider_int_mul_ovf = _consider_binop_symm
    consider_int_sub_ovf = _consider_binop
    consider_int_add_ovf = _consider_binop_symm

    def consider_int_add(self, op, position):
        y = op.getarg(1)
        if isinstance(y, ConstInt) and rx86.fits_in_32bits(y.value):
            pass # nothing to be hinted
        else:
            self._consider_binop_symm(op, position)

    consider_nursery_ptr_increment = consider_int_add

    def consider_int_lshift(self, op, position):
        x, y = op.getarg(0), op.getarg(1)
        if not isinstance(y, Const):
            self.longevity.fixed_register(position, ecx, y)
        if not isinstance(x, Const):
            self.longevity.try_use_same_register(x, op)

    consider_int_rshift  = consider_int_lshift
    consider_uint_rshift = consider_int_lshift

    def consider_uint_mul_high(self, op, position):
        # could do a lot more, but I suspect not worth it
        # just block eax and edx
        self.longevity.fixed_register(position, eax)
        self.longevity.fixed_register(position, edx)

    def consider_call_malloc_nursery(self, op, position):
        self.longevity.fixed_register(position, ecx, op)
        self.longevity.fixed_register(position, edx)

    consider_call_malloc_nursery_varsize = consider_call_malloc_nursery
    consider_call_malloc_nursery_varsize_frame = consider_call_malloc_nursery

    def _consider_call(self, op, position, guard_not_forced=False, first_arg_index=1):
        calldescr = op.getdescr()
        assert isinstance(calldescr, CallDescr)
        effectinfo = calldescr.get_extra_info()
        # XXX this is nonsense, share the code somehow
        if guard_not_forced:
            gc_level = 2
        elif effectinfo is None or effectinfo.check_can_collect():
            gc_level = 1
        else:
            gc_level = 0
        args = op.getarglist()[first_arg_index:]
        argtypes = calldescr.get_arg_types()
        CallHints64(self.longevity).hint(position, args, argtypes, gc_level)

    def _consider_real_call(self, op, position):
        effectinfo = op.getdescr().get_extra_info()
        assert effectinfo is not None
        oopspecindex = effectinfo.oopspecindex
        if oopspecindex != EffectInfo.OS_NONE:
            # XXX safe default: do nothing
            return
        self._consider_call(op, position)

    consider_call_i = _consider_real_call
    consider_call_r = _consider_real_call
    consider_call_f = _consider_real_call
    consider_call_n = _consider_real_call

oplist = [X86RegisterHints.not_implemented_op] * rop._LAST

for name, value in X86RegisterHints.__dict__.iteritems():
    if name.startswith('consider_'):
        name = name[len('consider_'):]
        num = getattr(rop, name.upper())
        oplist[num] = value



class CallHints64(object):

    ARGUMENTS_GPR = [edi, esi, edx, ecx, r8, r9]
    ARGUMENTS_XMM = [xmm0, xmm1, xmm2, xmm3, xmm4, xmm5, xmm6, xmm7]


    def __init__(self, longevity):
        self.longevity = longevity

    def _unused_gpr(self):
        i = self.next_arg_gpr
        self.next_arg_gpr = i + 1
        try:
            res = self.ARGUMENTS_GPR[i]
        except IndexError:
            return None
        return res

    def _unused_xmm(self):
        i = self.next_arg_xmm
        self.next_arg_xmm = i + 1
        try:
            return self.ARGUMENTS_XMM[i]
        except IndexError:
            return None

    def hint(self, position, args, argtypes, save_all_regs):
        hinted_xmm = []
        hinted_gpr = []
        hinted_args = []
        next_arg_gpr = 0
        next_arg_xmm = 0
        for i in range(len(args)):
            arg = args[i]
            if arg.type == "f" or (i < len(argtypes) and argtypes[i] == 'S'):
                if next_arg_xmm < len(self.ARGUMENTS_XMM):
                    tgt = self.ARGUMENTS_XMM[next_arg_xmm]
                    if not arg.is_constant() and arg not in hinted_args:
                        self.longevity.fixed_register(position, tgt, arg)
                        hinted_xmm.append(tgt)
                        hinted_args.append(arg)
                    next_arg_xmm += 1
            else:
                if next_arg_gpr < len(self.ARGUMENTS_GPR):
                    tgt = self.ARGUMENTS_GPR[next_arg_gpr]
                    if not arg.is_constant() and arg not in hinted_args:
                        self.longevity.fixed_register(position, tgt, arg)
                        hinted_gpr.append(tgt)
                        hinted_args.append(arg)
                    next_arg_gpr += 1
        # block all remaining registers that are not caller save
        # XXX the case save_all_regs == 1 (save callee-save regs + gc ptrs) is
        # no expressible atm
        if save_all_regs == 2:
            regs = X86_64_RegisterManager.all_regs
        else:
            regs = X86_64_RegisterManager.save_around_call_regs
        for reg in regs:
            if reg not in hinted_gpr:
                self.longevity.fixed_register(position, reg)
        for reg in X86_64_XMMRegisterManager.all_regs:
            if reg not in hinted_xmm:
                self.longevity.fixed_register(position, reg)
