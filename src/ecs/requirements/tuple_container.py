from src.ecs.requirements.execution_pair import ExecutionPair


class TupleContainer:
    def __init__(self, *reqs):
        self.tuple = reqs

    def __rshift__(self, other):
        return ExecutionPair(self.tuple, other)
