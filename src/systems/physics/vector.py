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
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other
        )

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * (1 / other)

    def squared_magnitude(self):
        return self.x ** 2 + self.y ** 2

    def __abs__(self):
        return self.squared_magnitude() ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __pow__(self, power, modulo=None):
        if power == 0:
            return self / abs(self) if self != Vector.zero else Vector.zero
        raise Exception

    def __invert__(self):
        return Vector(self.y, self.x)

    def project(self, other):
        return self * other / abs(other) * self ** 0


Vector.zero = Vector(0, 0)
