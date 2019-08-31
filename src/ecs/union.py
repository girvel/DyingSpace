class Entity:
    def __init__(self, *components):
        self.__components = components

        for component in components:
            name = type(component).__name__
            setattr(self, name[0].lower() + name[1:], component)

    def get_component(self, type_):
        return next((c for c in self.__components if isinstance(c, type_)), None)

    def has_component(self, type_):
        return self.get_component(type_) is not None
