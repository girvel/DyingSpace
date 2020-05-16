from src.ecs.requirements.has import has


VECTOR = "vector"
TEXT = "text"


def display(container):
    if container.display_type == VECTOR:
        container.size = container.display_func()
    elif container.display_type == TEXT:
        container.text = container.display_func()
    else:
        raise NotImplementedError


ui = (
    ("container" | has("display_func")) >> display,
)