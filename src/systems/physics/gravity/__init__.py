from src.ecs.clocks import delta_time
from src.ecs.requirements.has import has


def accelerate(self, other, constants):
    if self is other:
        return

    if not __debug__ and self.position == other.position:
        return

    delta = other.position - self.position
    self.velocity += delta ** 0 * other.mass / delta.squared_magnitude() * constants.G * delta_time()


massive = has("mass") & has("position") & has("velocity")
gravity = (
    ("self" | massive) * ("other" | massive) * ("constants" | has("G")) >> accelerate,
)
