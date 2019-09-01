class Vector:
    zero = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __neg__(self):
        return Vector(
            -self.x,
            -self.y
        )

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return Vector(
            self.x * other,
            self.y * other
        )

    def __rmul__(self, other):
        return self * other

    def squared_magnitude(self):
        return self.x ** 2 + self.y ** 2

    def magnitude(self):
        return self.squared_magnitude() ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


Vector.zero = Vector(0, 0)
