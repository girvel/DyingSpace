from src.ecs.requirements.execution_pair import ExecutionPair
from src.ecs.requirements.tuple_container import TupleContainer


class UnionRequirements:
    class Error(Exception):
        pass

    def __init__(self, name=None, requirements=None):
        self.name = name
        self.requirements = [] if requirements is None else requirements

    def __repr__(self):
        return f'({self.name} | {" & ".join(repr(r) for r in self.requirements)})'

    def __and__(self, other):
        return UnionRequirements(self.name, self.requirements + [other])

    def __rand__(self, other):
        return self & other

    def __ror__(self, other):
        if self.name is not None:
            raise UnionRequirements.Error("Requirements object already has a name")
        return UnionRequirements(other, self.requirements)

    def __mul__(self, other):
        if isinstance(other, TupleContainer):
            return TupleContainer(self, *other.tuple)

        return TupleContainer(self, other)

    def __rmul__(self, other):
        if isinstance(other, TupleContainer):
            return TupleContainer(*other.tuple, self)

        return TupleContainer(other, self)

    def __rshift__(self, other):
        return ExecutionPair((self, ), other)

    def match(self, o):
        if self.name is None:
            raise UnionRequirements.Error("Requirements object has no name")

        return {self.name: o} if all(r.match(o) for r in self.requirements) else None

    def size(self):
        return len(self.requirements)
