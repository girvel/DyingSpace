class EntityRequirement:
    def __init__(self, component_requirements):
        self.component_requirements = component_requirements

    def __mul__(self, other):
        if isinstance(other, tuple):
            return (self, ) + other

        if isinstance(other, EntityRequirement):
            return self * (other, )

        if isinstance(other, ComponentRequirement):
            return self * EntityRequirement([other])

        raise TypeError

    def __rmul__(self, other):
        return self * other


class ComponentRequirement:
    def __init__(self, name):
        self.name = name
        self.requirements = []

    def __or__(self, other):
        if len(self.requirements) > 0:
            raise TypeError

        self.requirements.append(other)
        return self

    def __and__(self, other):
        if len(self.requirements) == 0:
            raise TypeError

        self.requirements.append(other)
        return self

    def __mul__(self, other):
        return EntityRequirement([self]) * other

    def __add__(self, other):
        if isinstance(other, ComponentRequirement):
            return


class HasRequirement:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __ror__(self, other):
        if isinstance(other, str):
            return ComponentRequirement(other) | self


has = HasRequirement

method, attribute = range(2)
