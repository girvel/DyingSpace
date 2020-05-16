from src.ecs.clocks import delta_time
from src.ecs.requirements.has import has


def are_mounted(first, second):
    return (hasattr(first, 'mounting_object') and first.mounting_object is second) \
           or (hasattr(second, 'mounting_object') and second.mounting_object is first)


def mount(mounted):
    if not mounted.mounting_object:
        return

    parent = mounted.mounting_object

    # if mounted.mounting_force < abs(mounted.velocity - parent.velocity) * mounted.mass / delta_time():
    #     print('Mounting break with force', abs(mounted.velocity - parent.velocity) * mounted.mass / delta_time())
    #     mounted.mounting_object = None
    #     return

    if hasattr(mounted, "mass") and hasattr(parent, "mass"):
        parent.velocity = (mounted.mass * mounted.velocity + parent.mass * parent.velocity) \
                          / (mounted.mass + parent.mass)

    if hasattr(parent, "velocity"):
        mounted.velocity = parent.velocity

    rotation = parent.rotation if hasattr(parent, "rotation") else 0
    mounted.position = parent.position + mounted.mounting_offset.rotated(rotation)


mounting = (
    ("mounted" | has('mounting_object') & has('mounting_force')) >> mount,
)
