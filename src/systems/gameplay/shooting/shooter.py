class Shooter:
    def __init__(self, bullet_constructor, shooting_velocity, shooting_offset):
        self.bullet_constructor = bullet_constructor
        self.shooting_velocity = shooting_velocity
        self.shooting_offset = shooting_offset
        self.shooting_enabled = False
