from src.ecs.special_entities.named import name_of


class Union:
    class Error(Exception):
        pass

    def __init__(self, *components):
        self.registered = False

        for c in components:
            for attr_name in dir(c):

                if attr_name.startswith("__") or attr_name == 'registered':
                    continue

                attr_value = getattr(c, attr_name)

                if attr_name == 'union_init':
                    attr_value(self)
                    continue

                if callable(attr_value) and hasattr(type(c), attr_name):
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

    def where(self, **kw):
        result = Union(self)
        return result.set(**kw)

    def set(self, **kw):
        for name, value in kw.items():
            setattr(self, name, value)

        return self

    def __repr__(self):
        return name_of(self)

    def __bool__(self):
        return self is not None and self.registered
