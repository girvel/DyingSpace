from src.ecs.requirements.has import has

solid = has("radius", "solid")
destructor_ = has("clocks_destruction_list")


def stop_collisions(self, other, destructor):
    if self is other or not self.solid or not other.solid:
        return

    delta = other.position - self.position
    d = self.radius + other.radius
    if delta.x <= d \
            and delta.y <= d \
            and delta.squared_magnitude() <= d ** 2 \
            and self.velocity.scalar_project(delta) > other.velocity.scalar_project(delta):
        m1 = self.system_mass if hasattr(self, "system_mass") else self.mass if hasattr(self, "mass") else 0
        m2 = other.system_mass if hasattr(other, "system_mass") else other.mass if hasattr(other, "mass") else 0
        k = (1 + (self.resilience_k + other.resilience_k) / 2) / (m1 + m2)

        v1 = self.velocity.project(delta)
        v2 = other.velocity.project(delta)

        # result_velocity = (m * self.velocity + M * other.velocity) / (m + M)
        # self.velocity ==
        #
        # e_before = self.mass * self.velocity ** 2 / 2 + other.mass * other.velocity ** 2 / 2
        # e_after = (self.mass + other.mass) * result_velocity ** 2 / 2
        #
        # de = (e_before - e_after) / 2
        # print(f'energy is {de}')
        #

        dv1 = k * m2 * (v2 - v1)
        dv2 = k * m1 * (v1 - v2)

        self.velocity += dv1
        other.velocity += dv2

        if hasattr(self, "durability"):
            if m1 * dv1**2 >= 2 * self.durability:
                destructor.clocks_destruction_list.append(self)
            print(m1 * dv1**2 / 2)

        if hasattr(other, "durability"):
            if m2 * dv2**2 >= 2 * other.durability:
                destructor.clocks_destruction_list.append(other)
            print(m2 * dv2**2 / 2)


collision = (
    ("self" | solid) * ("other" | solid) * ("destructor" | destructor_) >> stop_collisions,
)
