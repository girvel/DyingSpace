from src.ecs.union import Union


def generate_create_function(clocks):
    def create(*components):
        e = Union(*components)
        clocks.register_entity(e)
        return e
    return create
