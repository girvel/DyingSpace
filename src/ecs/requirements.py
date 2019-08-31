attribute, method = range(2)


class HasRequirement:
    def __init__(self, type, name):
        self.attribute_name = name
        self.attribute_type = type

    def match(self, o):
        if not hasattr(o, self.attribute_name):
            return False
        if self.attribute_type == method:
            return callable(getattr(o, self.attribute_name))
        return True

    def __and__(self, other):
        return UnionRequirements(requirements=[self, other])

    def __ror__(self, other):
        return UnionRequirements(other, [self])


class UnionRequirements:
    class Error(Exception):
        pass

    def __init__(self, name=None, requirements=None):
        self.name = name
        self.requirements = [] if requirements is None else requirements

    def __and__(self, other):
        return UnionRequirements(self.name, self.requirements + [other])

    def __rand__(self, other):
        return self & other

    def __ror__(self, other):
        if self.name is not None:
            raise UnionRequirements.Error("Requirements object already has a name")
        return UnionRequirements(other, self.requirements)

    def __mul__(self, other):
        if isinstance(other, tuple):
            return (self, ) + other

        return self, other

    def __rmul__(self, other):
        if isinstance(other, tuple):
            return other + (self, )

        return other, self

    def match(self, o):
        if self.name is None:
            raise UnionRequirements.Error("Requirements object has no name")

        return {self.name: o} if all(r.match(o) for r in self.requirements) else None


has = HasRequirement
