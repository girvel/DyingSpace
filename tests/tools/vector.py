from math import sqrt, pi
from unittest import TestCase, main

from src.tools.vector import Vector


class VectorTests(TestCase):
    def test_project(self):
        self.assertEqual(Vector(1, 0).project(Vector(0, 1)), Vector.zero)
        self.assertEqual(Vector(3, 4).project(Vector(0, 1)), Vector(0, 4))

    def test_scalar_project(self):
        self.assertEqual(Vector(1, 1).scalar_project(Vector(-1, 0)), -1)

    def test_angle(self):
        self.assertAlmostEqual(Vector(1, -1).angle(), -pi / 4, delta=0.01)


if __name__ == '__main__':
    main()
