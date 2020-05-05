from src.ecs.requirements.has import has

fps_monitor = (
    ("label" | has("update_fps")) >> (lambda label: label.update_fps()),
)