import json

from src.systems.physics.tools import distance_vector


class DefaultDataCollector:
    def __init__(self, path, language):
        self.path = path
        with open(self.path, encoding="UTF-8") as f:
            self.texts = json.load(f)
        self.language = language

    def get_text(self, name):
        return self.texts[self.language][name]

    def get_vector_data(self):
        return (
            (self.get_text("speed"), lambda: self.velocity / 1000, "lightgreen"),
            (self.get_text("distance"), lambda: distance_vector(self, self.navigation_target) / 1000, "red")
        )

    def get_scalar_data(self):
        return (
            (self.get_text("mass"), lambda: self.mass / 1000, "green"),
            (self.get_text("traction_force"), lambda: self.traction_force / 1000, "green"),
            (self.get_text("durability"), lambda: self.durability / 1e6, "green"),
        )

    def get_string_data(self):
        target = self.navigation_target
        return (
            (lambda: self.get_text("target").format(target.name if hasattr(target, "name") else "<unknown>"), "red"),
            *(
                ((lambda l: lambda: l)(line), "green") for line in self.get_text("guide")
            )
        )

    def __repr__(self):
        return "{DefaultDataCollector}"
