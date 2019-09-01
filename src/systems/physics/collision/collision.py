from src.ecs.requirements import attribute, has
from src.systems.physics.vector import Vector

solid = has(attribute, "radius") & has(attribute, "position") & has(attribute, "velocity")


def stop_collisions(self, other):
    if self is other:
        return

    delta = other.position - self.position
    if delta.squared_magnitude() <= (self.radius + other.radius) ** 2:
        self.velocity = Vector.zero
        print("collision")


collision = (
    ("self" | solid) * ("other" | solid) >> stop_collisions,
)
