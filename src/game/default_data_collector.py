from src.systems.physics.tools import distance_vector


class DefaultDataCollector:
    def get_vector_data(self):
        return \
            ("$speed = {0} km/s", self.velocity / 1000, "lightgreen"), \
            ("$distance_to_target = {0} km", distance_vector(self, self.navigation_target) / 1000, "red")

    def get_scalar_data(self):
        return \
            ("$mass = {0} tn", self.mass / 1000, "green"), \
            ("$traction_force = {0} kN", self.traction_force / 1000, "green"), \
            ("$durability = {0} M", self.durability / 1e6, "green"),

    def get_string_data(self):
        target = self.navigation_target
        return \
            ('$target = ' + (target.name if hasattr(target, "name") else "<unknown>"), "red"), \
            ('    W to launch engine', 'green'), \
            ('    S to stop it', 'green'), \
            ('    A/D to rotate spaceship', 'green'), \
            ('    Dont forget to buckle your seat belts', 'green'), \
            ('    and switch system language', 'green')

    def __repr__(self):
        return "{DefaultDataCollector}"
