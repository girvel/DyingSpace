from src.ecs.requirements.union import UnionRequirements


class HasRequirement:
    def __init__(self, *attributes):
        self.attributes = attributes

    def __repr__(self):
        return f"has '{self.attributes}'"

    def match(self, o):
        if not all(hasattr(o, a) for a in self.attributes):
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
