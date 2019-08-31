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
        union = Union(A, B)

        # assert
        self.assertEqual(union.a, 12)
        self.assertEqual(union.b, 13)

    def test_union_throws_error_when_one_of_constructors_has_arguments(self):
        # arrange
        class A:
            def __init__(self):
                self.a = 12

        class B:
            def __init__(self, b):
                self.b = b

        # assert
        self.assertRaises(Union.Error, lambda: Union(A, B))

    def test_union_throws_error_when_components_have_common_attributes(self):
        # arrange
        class A:
            def a(self):
                pass

        class B:
            def a(self, b):
                pass

        # assert
        self.assertRaises(Union.Error, lambda: Union(A, B))


if __name__ == '__main__':
    main()
