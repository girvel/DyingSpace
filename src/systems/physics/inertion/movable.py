from src.tools import vector


class Movable:
    def __init__(self, velocity=vector.zero):
        self.velocity = velocity
