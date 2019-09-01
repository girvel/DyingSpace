from src.systems.physics.vector import Vector


class Movable:
    def __init__(self, velocity=Vector.zero):
        self.velocity = velocity
