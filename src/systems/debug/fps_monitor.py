from src.ecs.requirements import has, method

fps_monitor = (
    ("label" | has(method, "update_fps")) >> (lambda label: label.update_fps()),
)
