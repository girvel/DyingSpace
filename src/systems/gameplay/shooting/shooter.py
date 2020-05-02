class Shooter:
    def __init__(self, bullet_prototype, shooting_energy, shooting_offset):
        self.bullet_prototype = bullet_prototype
        self.shooting_energy = shooting_energy
        self.shooting_offset = shooting_offset
        self.shooting_enabled = False
