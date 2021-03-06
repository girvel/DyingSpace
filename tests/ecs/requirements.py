from unittest import TestCase, main

from src.ecs.requirements.execution_pair import mul
from src.ecs.requirements.has import has
from src.ecs.requirements.execution_pair import ExecutionPair
from src.ecs.requirements.union import UnionRequirements


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

        h = has("t")

        # assert
        self.assertTrue(h.match(A()))
        self.assertFalse(h.match(B()))

    def test_has_and_has(self):
        # arrange
        h1 = has("a")
        h2 = has("b")
        h3 = has("c")
        h = h1 & h2 & h3

        # assert
        self.assertIs(h.name, None)
        self.assertListEqual(h.requirements, [h1, h2, h3])

    def test_union_requirements_ror(self):
        # arrange
        h1 = has("a")
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

        h1 = has("a")
        h2 = has("b")
        h = "u" | h1 & h2

        # assert
        self.assertTrue(h.match(A()))
        self.assertIsInstance(h.match(A())["u"], A)
        self.assertFalse(h.match(B()))
        self.assertRaises(UnionRequirements.Error, lambda: (h1 & h2).match(A()))

    def test_union_requirements_multiplication(self):
        # arrange
        ur1 = UnionRequirements("a", [has("a"), has("b")])
        ur2 = UnionRequirements("b", [has("c"), has("b")])

        # act
        t = ur1 * ur1 * ur2

        # assert
        self.assertEqual(t.tuple, (ur1, ur1, ur2))

    def test_mul(self):
        # arrange
        c1 = [1, 2, 3]
        c2 = [1]
        c3 = [4, 5]

        # act
        subjects = mul((c1, c2, c3))

        # assert
        self.assertListEqual(
            list(subjects),
            [
                (1, 1, 4),
                (1, 1, 5),
                (2, 1, 4),
                (2, 1, 5),
                (3, 1, 4),
                (3, 1, 5),
            ]
        )

    def test_execution_pair_creation(self):
        # arrange
        ur = UnionRequirements()
        def m(): pass

        # act
        ep = ur >> m

        # assert
        self.assertEqual(ep.requirements, (ur, ))
        self.assertEqual(ep.action, m)

    def test_execution_pair_subjects_addition(self):
        # arrange
        class A:
            def a(self): pass

        class B:
            def b(self): pass

        class C(A, B): pass

        pair = ExecutionPair(
            ("f" | has("a")) * ("s" | has("b")),
            lambda f, s: None
        )

        a1 = A()
        a2 = A()
        b1 = B()

        pair.subjects = [
            {"f": a1, "s": b1},
            {"f": a2, "s": b1},
        ]
        pair.subjects = (
            _Cache("f", [a1, a2]),
            _Cache("s", [b1]),
        )

        a3 = A()
        c = C()

        # act
        pair.try_add_subject(a3)
        pair.try_add_subject(c)

        # assert
        self.assertListEqual(
            pair.subjects,
            [
                {"f": a1, "s": b1},
                {"f": a2, "s": b1},
                {"f": a3, "s": b1},
                {"f": c,  "s": b1},
                {"f": a1, "s": c},
                {"f": a2, "s": c},
                {"f": a3, "s": c},
                {"f": c,  "s": c},
            ]
        )


if __name__ == '__main__':
    main()
