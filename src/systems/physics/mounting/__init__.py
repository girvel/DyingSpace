from src.ecs.clocks import delta_time
from src.ecs.requirements.has import has


def mount(mounted):
    if not mounted.mounting_object:
        return

    parent = mounted.mounting_object

    # if mounted.mounting_force < abs(mounted.velocity - parent.velocity) * mounted.mass / delta_time():
    #     print('Mounting break with force', abs(mounted.velocity - parent.velocity) * mounted.mass / delta_time())
    #     mounted.mounting_object = None
    #     return

    mounted.velocity = (mounted.mass * mounted.velocity + parent.mass * parent.velocity) / (mounted.mass + parent.mass)
    parent.velocity = mounted.velocity

    mounted.position = parent.position + mounted.mounting_offset.rotated(parent.rotation)


mounting = (
    ("mounted" | has('mounting_object') & has('mounting_force')) >> mount,
)
