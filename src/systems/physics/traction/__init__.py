from src.ecs.clocks import delta_time
from src.ecs.requirements import has


def apply_force(tractor):
    if tractor.traction_enabled:
        tractor.velocity += \
            tractor.traction_direction.rotated(
                tractor.rotation
                if hasattr(tractor, "rotation") else 0) \
            * tractor.traction_force \
            * delta_time() \
            / tractor.mass


traction = (
    ("tractor" |
     has("velocity") &
     has("traction_force") &
     has("traction_direction") &
     has("mass")
     ) >> apply_force,
)
