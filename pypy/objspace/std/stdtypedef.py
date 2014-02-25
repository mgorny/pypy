from pypy.interpreter.baseobjspace import SpaceCache


class TypeCache(SpaceCache):
    def build(cache, typedef):
        "NOT_RPYTHON: initialization-time only."
        # build a W_TypeObject from this StdTypeDef
        from pypy.objspace.std.typeobject import W_TypeObject
        from pypy.objspace.std.objectobject import W_ObjectObject

        space = cache.space
        w = space.wrap
        rawdict = typedef.rawdict
        lazyloaders = {}

        # compute the bases
        if typedef is W_ObjectObject.typedef:
            bases_w = []
        else:
            bases = typedef.bases or [W_ObjectObject.typedef]
            bases_w = [space.gettypeobject(base) for base in bases]

        # wrap everything
        dict_w = {}
        for descrname, descrvalue in rawdict.items():
            dict_w[descrname] = w(descrvalue)

        if typedef.applevel_subclasses_base is not None:
            overridetypedef = typedef.applevel_subclasses_base.typedef
        else:
            overridetypedef = typedef
        w_type = W_TypeObject(space, typedef.name, bases_w, dict_w,
                              overridetypedef=overridetypedef)
        if typedef is not overridetypedef:
            w_type.w_doc = space.wrap(typedef.doc)
        w_type.lazyloaders = lazyloaders
        return w_type

    def ready(self, w_type):
        w_type.ready()
