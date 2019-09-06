from unittest import TestCase, main

from src.ecs.union import Union


class UnionTests(TestCase):
    def test_union_combines_classes(self):
        # arrange
        class A:
            def __init__(self):
                self.a = 12

        class B:
            def __init__(self):
                self.b = 13

        # act
        union = Union(A(), B())

        # assert
        self.assertEqual(union.a, 12)
        self.assertEqual(union.b, 13)

    def test_union_raises_error_when_components_have_common_attributes(self):
        # arrange
        class A:
            def a(self):
                pass

        class B:
            def a(self, b):
                pass

        # assert
        self.assertRaises(Union.Error, lambda: Union(A(), B()))

    def test_union_combines_methods(self):
        # arrange
        class A:
            def __init__(self):
                self.a = 10

        class B:
            def b(self): return self.a

        union = Union(A(), B())

        # act
        v = union.b()

        # assert
        self.assertEqual(v, 10)

    def test_union_calls_union_init(self):
        # arrange
        class A:
            def __init__(self, a):
                self.a = a

            def union_init(self, union):
                union.b = self.a ** 2

        # act
        union = Union(A(10))

        # assert
        self.assertFalse(hasattr(union, "union_init"))
        self.assertEqual(union.b, 100)


if __name__ == '__main__':
    main()
