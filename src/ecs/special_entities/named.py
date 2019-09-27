class Named:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'named "{self.name}"'


def name_of(union):
    if union is None:
        return str(None)

    if not hasattr(union, "name"):
        return "<Union>"

    return f'<{union.name}>'
