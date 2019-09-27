class Union:
    class Error(Exception):
        pass

    def __init__(self, *components):
        self.__repr_sources = []

        for c in components:
            for attr_name in dir(c):
                if attr_name == "__repr__":
                    self.__repr_sources.append(type(c).__repr__)

                if attr_name.startswith("__"):
                    continue

                attr_value = getattr(c, attr_name)

                if attr_name == 'union_init':
                    attr_value(self)
                    continue

                if callable(attr_value):
                    setattr(
                        self,
                        attr_name,
                        (lambda method:
                            lambda *args, **kw: method(self, *args, **kw)
                         )(getattr(type(c), attr_name))
                    )
                    continue

                if hasattr(self, attr_name):
                    raise Union.Error(f"Components have common attribute {attr_name}")

                setattr(self, attr_name, attr_value)

    def __repr__(self):
        return "{{Union: {0}}}".format(", ".join(r(self) for r in self.__repr_sources))
