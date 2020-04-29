from src.ecs.clocks import delta_time
from src.ecs.requirements.has import has


def mount(mounted):
    if not mounted.mounting_object:
        return

    if mounted.mounting_force < abs(mounted.velocity - mounted.mounting_object.velocity) / delta_time() * mounted.mass:
        mounted.mounting_object = None
        return

    mounted.velocity = mounted.mounting_object.velocity


mounting = (
    ("mounted" | has('mounting_object') & has('velocity') & has('mounting_force') & has('mass')) >> mount,
)
