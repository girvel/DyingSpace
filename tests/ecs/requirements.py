from unittest import TestCase, main

from src.ecs.requirements import has, method, UnionRequirements


class RequirementsTests(TestCase):
    def test_match_checks_attribute_existence(self):
        # arrange
        class A:
            def __init__(self):
                self.a = 1

            def t(self):
                pass

        class B:
            def a(self):
                pass

        h = has(method, "t")

        # assert
        self.assertTrue(h.match(A()))
        self.assertFalse(h.match(B()))

    def test_has_and_has(self):
        # arrange
        h1 = has(method, "a")
        h2 = has(method, "b")
        h3 = has(method, "c")
        h = h1 & h2 & h3

        # assert
        self.assertIs(h.name, None)
        self.assertListEqual(h.requirements, [h1, h2, h3])

    def test_union_requirements_ror(self):
        # arrange
        h1 = has(method, "a")
        h = "B" | h1

        # assert
        self.assertRaises(UnionRequirements.Error, lambda: "C" | h)
        self.assertEqual(h.name, "B")
        self.assertListEqual(h.requirements, [h1])

    def test_union_requirement_match_works(self):
        # arrange
        class A:
            def a(self): pass

            def b(self): pass

        class B:
            def a(self): pass

        h1 = has(method, "a")
        h2 = has(method, "b")
        h = "u" | h1 & h2

        # assert
        self.assertTrue(h.match(A()))
        self.assertIsInstance(h.match(A())["u"], A)
        self.assertFalse(h.match(B()))
        self.assertRaises(UnionRequirements.Error, lambda: (h1 & h2).match(A()))

    def test_union_requirements_multiplication(self):
        # arrange
        ur1 = UnionRequirements("a", [has(method, "a"), has(method, "b")])
        ur2 = UnionRequirements("b", [has(method, "c"), has(method, "b")])

        # act
        t = ur1 * ur1 * ur2

        # assert
        self.assertEqual(t, (ur1, ur1, ur2))


if __name__ == '__main__':
    main()
