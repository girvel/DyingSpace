from src.ecs.requirements import has, attribute

solid = has(attribute, "radius") & has(attribute, "position") & has(attribute, "velocity")
destructor_ = has(attribute, "clocks_destruction_list")


def stop_collisions(self, other, destructor):
    if self is other:
        return

    delta = other.position - self.position
    if delta.squared_magnitude() <= (self.radius + other.radius) ** 2:
        if hasattr(self, "durability") and hasattr(self, "mass"):
            movement_energy = (self.mass * self.velocity ** 2) / 2
            print(f'energy is {movement_energy}')
            if movement_energy >= self.durability:
                destructor.clocks_destruction_list.append(self)

        self.velocity *= 0


collision = (
    ("self" | solid) * ("other" | solid) * ("destructor" | destructor_) >> stop_collisions,
)
