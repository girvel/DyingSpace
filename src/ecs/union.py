class Union:
    class Error(Exception):
        pass

    def __init__(self, *components):
        for c in components:
            try:
                c.__init__(self)
            except TypeError:
                raise Union.Error("Components' constructors should have no arguments")

            for attribute in dir(c):
                if attribute.startswith("__"):
                    continue

                if hasattr(self, attribute):
                    raise Union.Error(f"Components have common attribute {attribute}")

                setattr(self, attribute, getattr(c, attribute))
