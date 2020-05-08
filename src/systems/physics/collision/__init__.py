from src.ecs.requirements.has import has

solid = has("radius") & has("position") & has("velocity") & has("solid")
destructor_ = has("clocks_destruction_list")


def stop_collisions(self, other, destructor):
    if self is other or not self.solid or not other.solid:
        return

    delta = other.position - self.position
    d = self.radius + other.radius
    if delta.x <= d and delta.y <= d and delta.squared_magnitude() <= d ** 2 and self.velocity != other.velocity:
        m = self.mass if hasattr(self, "mass") else 0
        M = other.mass if hasattr(other, "mass") else 0

        result_velocity = (m * self.velocity + M * other.velocity) / (m + M)

        e_before = self.mass * self.velocity ** 2 / 2 + other.mass * other.velocity ** 2 / 2
        e_after = (self.mass + other.mass) * result_velocity ** 2 / 2

        de = (e_before - e_after) / 2
        print(f'energy is {de}')

        if hasattr(self, "durability"):
            if de >= self.durability:
                destructor.clocks_destruction_list.append(self)

        if hasattr(other, "durability"):
            if de >= other.durability:
                destructor.clocks_destruction_list.append(other)

        self.velocity = result_velocity
        other.velocity = result_velocity


collision = (
    ("self" | solid) * ("other" | solid) * ("destructor" | destructor_) >> stop_collisions,
)
