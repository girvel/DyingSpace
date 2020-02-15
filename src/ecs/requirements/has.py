from src.ecs.requirements.union import UnionRequirements


class HasRequirement:
    def __init__(self, name):
        self.attribute_name = name

    def __repr__(self):
        return f"has '{self.attribute_name}'"

    def match(self, o):
        if not hasattr(o, self.attribute_name):
            return False
        return True

    def __and__(self, other):
        return UnionRequirements(requirements=[self, other])

    def __ror__(self, other):
        return UnionRequirements(other, [self])

    @staticmethod
    def size():
        return 1


has = HasRequirement
