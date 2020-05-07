from src.ecs.requirements.has import has


def display(container):
    container.position = container.debug_subject.position
    container.size = container.debug_func(container.debug_subject)


data_display = (
    ("container" | has("debug_subject") & has("debug_func")) >> display,
)
