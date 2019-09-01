from src.ecs.clocks import delta_time
from src.ecs.requirements import attribute, has


def accelerate(self, other, constants):
    if self is other:
        return

    if not __debug__ and self.position == other.position:
        return

    delta = other.position - self.position
    self.velocity += ~delta * other.mass / delta.squared_magnitude() * constants.G * delta_time()


massive = has(attribute, "mass") & has(attribute, "position") & has(attribute, "velocity")

gravity = (
    ("self" | massive) * ("other" | massive) * ("constants" | has(attribute, "G")) >> accelerate,
)
