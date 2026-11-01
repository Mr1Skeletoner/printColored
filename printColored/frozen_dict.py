import builtins

if hasattr(builtins, "frozendict"):          
    frozendict = builtins.frozendict
else:
    try:
        from frozendict import frozendict    # PyPI backport
    except ImportError:                      
        class frozendict(dict):
            __slots__ = ()

            def _readonly(self, *args, **kwargs):
                raise TypeError(f"'{type(self).__name__}' object is immutable")

            __setitem__ = __delitem__ = __ior__ = _readonly
            clear = pop = popitem = setdefault = update = _readonly

            def __hash__(self):
                return hash(frozenset(self.items()))