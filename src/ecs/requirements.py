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

    @staticmethod
    def size():
        return 1


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


class TupleContainer:
    def __init__(self, *reqs):
        self.tuple = reqs

    def __rshift__(self, other):
        return ExecutionPair(self.tuple, other)


class _Cache:
    def __init__(self, name, collection=None):
        self.collection = [] if collection is None else collection
        self.name = name


def mul(*caches):
    if not caches:
        return [dict()]

    result = []

    for e in caches[0].collection:
        for rest in mul(*caches[1:]):
            result.append({caches[0].name: e, **rest})

    return result


class ExecutionPair:
    def __init__(self, requirements, action):
        self.requirements = requirements
        self.action = action
        self.subjects = []
        self.caches = tuple(_Cache(req.name) for req in requirements)

    def try_add_subject(self, subject):
        for i, req in enumerate(self.requirements):
            match = req.match(subject)

            if not match:
                continue

            self.subjects.extend(mul(
                *self.caches[:i],
                _Cache(
                    self.caches[i].name,
                    match.values()
                ),
                *self.caches[i + 1:]
            ))

            self.caches[i].collection.append(subject)

    def execute(self):
        for s in self.subjects:
            self.action(**s)


has = HasRequirement