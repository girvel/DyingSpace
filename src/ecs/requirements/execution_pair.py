class ExecutionPair:
    def __init__(self, requirements, action):
        self.requirements = requirements
        self.action = action
        self.subjects = tuple([] for _ in self.requirements)
        self.caches = []

    def __repr__(self):
        return f'{{ExecutionPair: {repr(self.requirements)} >> {self.action.__name__}}}'

    def try_add_subject(self, subject):
        for i, req in enumerate(self.requirements):
            match = req.match(subject)

            if not match:
                continue

            self.subjects[i].append(subject)

            self.caches.extend(mul((
                *self.subjects[:i],
                [subject],
                *self.subjects[i + 1:]
            )))

    def try_remove_subject(self, subject):
        for i, req in enumerate(self.requirements):
            match = req.match(subject)

            if not match:
                continue

            if subject in self.subjects[i]:
                self.subjects[i].remove(subject)
                self.caches = [cache for cache in self.caches if all(arg != subject for arg in cache)]

    def execute(self):
        for c in self.caches:
            self.action(*c)


def mul(lists, i0=0):
    for item in lists[i0]:
        if i0 == len(lists) - 1:
            yield item,
        else:
            for rest_items in mul(lists, i0 + 1):
                yield (item, *rest_items)
