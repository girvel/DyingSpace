from src.ecs.requirements.has import has
from src.ecs.union import Union

data_types = Union(
    vector="vector",
    text="text",
)


def display(container):
    if container.display_type == data_types.vector:
        container.size = container.display_func()
    elif container.display_type == data_types.text:
        container.text = container.display_func()
    else:
        raise NotImplementedError


ui = (
    ("container" | has("display_func")) >> display,
)