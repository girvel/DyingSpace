from src.ecs.clocks import delta_time
from src.ecs.requirements.has import has


def precalculate(self, constants):
    self.squared_gravity_radius = self.mass / constants.g_min / constants.G


def accelerate(self, other, constants):
    if self is other:
        return

    assert self.position != other.position

    delta = other.position - self.position

    if delta.squared_magnitude() > self.squared_gravity_radius:
        return

    self.velocity += delta ** 0 * other.mass / delta.squared_magnitude() * constants.G * delta_time()


massive = has("mass") & has("position") & has("velocity")
gravity = (
    ("self" | massive) * ("constants" | has("g_min") & has("G")) >> precalculate,
    ("self" | massive) * ("other" | massive) * ("constants" | has("G")) >> accelerate,
)
