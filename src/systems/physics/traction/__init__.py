from src.ecs.clocks import delta_time
from src.ecs.requirements import has, attribute


def apply_force(tractor):
    if tractor.traction_enabled:
        tractor.velocity += tractor.traction_direction * tractor.traction_force / tractor.mass * delta_time()


traction = (
    ("tractor" |
     has(attribute, "velocity") &
     has(attribute, "traction_force") &
     has(attribute, "traction_direction") &
     has(attribute, "mass")
     ) >> apply_force,
)
