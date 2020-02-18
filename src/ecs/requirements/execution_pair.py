from src.ecs.requirements.cache import _Cache, mul


class ExecutionPair:
    def __init__(self, requirements, action):
        self.requirements = requirements
        self.action = action
        self.subjects = []
        self.caches = tuple(_Cache(req.name) for req in requirements)

    def __repr__(self):
        return f'{{ExecutionPair: {repr(self.requirements)} >> {self.action.__name__}}}'

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

    def try_remove_subject(self, subject):
        for i, req in enumerate(self.requirements):
            match = req.match(subject)

            if not match:
                continue

            if subject in self.caches[i].collection:
                self.caches[i].collection.remove(subject)
                self.subjects = [s for s in self.subjects if all(v != subject for k, v in s.items())]

    def execute(self):
        for s in self.subjects:
            self.action(**s)
