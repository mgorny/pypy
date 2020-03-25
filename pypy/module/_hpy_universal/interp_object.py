from rpython.rtyper.lltypesystem import lltype, rffi
from pypy.interpreter.error import OperationError, oefmt
import pypy.module.__builtin__.operation as operation
from pypy.module._hpy_universal.apiset import API
from pypy.module._hpy_universal import handles

def charp2text(space, ptr):
    s = rffi.charp2str(ptr)
    return space.newtext(s)

@API.func("HPy HPy_GetAttr(HPyContext ctx, HPy obj, HPy h_name)")
def HPy_GetAttr(space, ctx, h_obj, h_name):
    w_obj = handles.deref(space, h_obj)
    w_name = handles.deref(space, h_name)
    w_res = space.getattr(w_obj, w_name)
    return handles.new(space, w_res)


@API.func("HPy HPy_GetAttr_s(HPyContext ctx, HPy h_obj, const char *name)")
def HPy_GetAttr_s(space, ctx, h_obj, name):
    w_obj = handles.deref(space, h_obj)
    w_name = charp2text(space, name)
    w_res = space.getattr(w_obj, w_name)
    return handles.new(space, w_res)


@API.func("int HPy_HasAttr(HPyContext ctx, HPy h_obj, HPy h_name)")
def HPy_HasAttr(space, ctx, h_obj, h_name):
    w_obj = handles.deref(space, h_obj)
    w_name = handles.deref(space, h_name)
    return _HasAttr(space, w_obj, w_name)

@API.func("int HPy_HasAttr_s(HPyContext ctx, HPy h_obj, const char *name)")
def HPy_HasAttr_s(space, ctx, h_obj, name):
    w_obj = handles.deref(space, h_obj)
    w_name = charp2text(space, name)
    return _HasAttr(space, w_obj, w_name)

def _HasAttr(space, w_obj, w_name):
    try:
        w_res = operation.hasattr(space, w_obj, w_name)
        return rffi.cast(rffi.INT_real, space.is_true(w_res))
    except OperationError:
        return rffi.cast(rffi.INT_real, 0)


@API.func("int HPy_SetAttr(HPyContext ctx, HPy h_obj, HPy name, HPy value)")
def HPy_SetAttr(space, ctx, h_obj, name, value):
    from rpython.rlib.nonconst import NonConstant # for the annotator
    if NonConstant(False): return 0
    raise NotImplementedError

@API.func("int HPy_SetAttr_s(HPyContext ctx, HPy h_obj, const char *name, HPy value)")
def HPy_SetAttr_s(space, ctx, h_obj, name, value):
    from rpython.rlib.nonconst import NonConstant # for the annotator
    if NonConstant(False): return 0
    raise NotImplementedError

@API.func("HPy HPy_GetItem(HPyContext ctx, HPy h_obj, HPy key)")
def HPy_GetItem(space, ctx, h_obj, key):
    from rpython.rlib.nonconst import NonConstant # for the annotator
    if NonConstant(False): return 0
    raise NotImplementedError

@API.func("HPy HPy_GetItem_i(HPyContext ctx, HPy h_obj, HPy_ssize_t idx)")
def HPy_GetItem_i(space, ctx, h_obj, idx):
    from rpython.rlib.nonconst import NonConstant # for the annotator
    if NonConstant(False): return 0
    raise NotImplementedError

@API.func("HPy HPy_GetItem_s(HPyContext ctx, HPy h_obj, const char *key)")
def HPy_GetItem_s(space, ctx, h_obj, key):
    from rpython.rlib.nonconst import NonConstant # for the annotator
    if NonConstant(False): return 0
    raise NotImplementedError

@API.func("int HPy_SetItem(HPyContext ctx, HPy h_obj, HPy key, HPy value)")
def HPy_SetItem(space, ctx, h_obj, key, value):
    from rpython.rlib.nonconst import NonConstant # for the annotator
    if NonConstant(False): return 0
    raise NotImplementedError

@API.func("int HPy_SetItem_i(HPyContext ctx, HPy h_obj, HPy_ssize_t idx, HPy value)")
def HPy_SetItem_i(space, ctx, h_obj, idx, value):
    from rpython.rlib.nonconst import NonConstant # for the annotator
    if NonConstant(False): return 0
    raise NotImplementedError

@API.func("int HPy_SetItem_s(HPyContext ctx, HPy h_obj, const char *key, HPy value)")
def HPy_SetItem_s(space, ctx, h_obj, key, value):
    from rpython.rlib.nonconst import NonConstant # for the annotator
    if NonConstant(False): return 0
    raise NotImplementedError
