from src.ecs.clocks import delta_time
from src.ecs.requirements.has import has


def mount(mounted):
    if not mounted.mounting_object:
        return

    # if mounted.mounting_force < abs(mounted.velocity - mounted.mounting_object.velocity) * mounted.mass / delta_time():
    #     print('Mounting break with force', abs(mounted.velocity - mounted.mounting_object.velocity) * mounted.mass / delta_time())
    #     mounted.mounting_object = None
    #     return

    mounted.position = mounted.mounting_object.position + mounted.mounting_offset.rotated(mounted.mounting_object.rotation)


mounting = (
    ("mounted" | has('mounting_object') & has('mounting_force')) >> mount,
)
