from src.ecs.union import Union


def generate_create_function(clocks):
    def create(*components):
        e = Union(*components)
        clocks.register_entity(e)
        return e
    return create


def generate_where(_class):
    def _where(self, **kw):
        for key, value in kw.items():
            setattr(self, key, value)
        return self

    _class.where = _where
