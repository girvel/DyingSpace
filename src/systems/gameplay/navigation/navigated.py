from src.ecs.special_entities.named import name_of


class Navigated:
    def __init__(self, navigation_target):
        self.navigation_target = navigation_target

    def __repr__(self):
        return f'{{Navigated: {name_of(self.navigation_target)}}}'
