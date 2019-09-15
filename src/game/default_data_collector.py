from src.systems.physics.tools import distance_vector


class DefaultDataCollector:
    def get_combined_data(self):
        return \
            (self.velocity / 1000, "speed", "lightgreen", "km/s"), \
            (distance_vector(self, self.navigation_target) / 1000, "distance_to_target", "red", "km")

    def get_numeric_data(self):
        return \
            (self.mass / 1000, "mass", "green", "tn"), \
            (self.traction_force / 1000, "traction_force", "green", "kN"), \
            (self.durability / 1e6, "durability", "green", "M"),

    def get_string_data(self):
        target = self.navigation_target
        return (target.name if hasattr(target, "name") else "<unknown>", "target", "red", ""),
