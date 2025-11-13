import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):
    def test_factorial_positive_numbers(self):
        result = factorial(3)
        self.assertEqual(result, 6)

    def test_factorial_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            factorial(-3)
        self.assertEqual(str(context.exception), "Factorial is not defined for negative numbers.")

    def test_factorial_zero(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_factorial_one(self):
        result = factorial(1)
        self.assertEqual(result, 1)

    def test_factorial_larger_numbers(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(4), 24)


if __name__ == '__main__':
    unittest.main()