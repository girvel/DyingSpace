class _Cache:
    def __init__(self, name, collection=None):
        self.collection = [] if collection is None else collection
        self.name = name

    def __repr__(self):
        return f'{{_Cache "{self.name}"}}'


def mul(*caches):
    if not caches:
        return [dict()]

    result = []

    for e in caches[0].collection:
        for rest in mul(*caches[1:]):
            result.append({caches[0].name: e, **rest})

    return result
