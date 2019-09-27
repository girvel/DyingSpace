class Navigated:
    def __init__(self, navigation_target):
        self.navigation_target = navigation_target

    def __repr__(self):
        return f'{{Navigated: {self.navigation_target.name if hasattr(self.navigation_target, "name") else ""}}}'
