from unittest import TestCase, main

from src.tools.limited import Limited


class LimitedTests(TestCase):
    def test_limited_step(self):
        # arrange
        limited = Limited(10, 0, 20)

        # act
        limited.step(40)

        # assert
        self.assertEqual(limited.value, 20)

    def test_limited_step_negative(self):
        # arrange
        limited = Limited(10, 0, 20)

        # act
        limited.step(-12)

        # assert
        self.assertEqual(limited.value, 0)

    def test_limited_to_proportion(self):
        # arrange
        limited = Limited(10, -10, 20)

        # assert
        self.assertEqual(limited.to_proportion(), 2/3)


if __name__ == '__main__':
    main()
