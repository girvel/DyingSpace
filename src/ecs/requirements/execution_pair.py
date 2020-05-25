class ExecutionPair:
    def __init__(self, requirements, action):
        self.requirements = requirements
        self.action = action
        self.subjects = tuple([] for _ in self.requirements)

    def __repr__(self):
        return f'{{ExecutionPair: {repr(self.requirements)} >> {self.action.__name__}}}'

    def try_add_subject(self, subject):
        for i, req in enumerate(self.requirements):
            match = req.match(subject)

            if not match:
                continue

            self.subjects[i].append(subject)

    def try_remove_subject(self, subject):
        for i, req in enumerate(self.requirements):
            match = req.match(subject)

            if not match:
                continue

            if subject in self.subjects[i]:
                self.subjects[i].remove(subject)

    def execute(self):
        for s in mul(self.subjects):
            self.action(*s)


def mul(lists, i0=0):
    for item in lists[i0]:
        if i0 == len(lists) - 1:
            yield item,
        else:
            for rest_items in mul(lists, i0 + 1):
                yield (item, *rest_items)
