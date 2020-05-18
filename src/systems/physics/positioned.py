from src.tools.vector import Vector


class Positioned:
    def __init__(self, position=None):
        self.position = position if position else vector.zero
