import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fibo import fibonacci_sequence


class TestFibonacci(unittest.TestCase):
    def test_basic_fibonacci(self):
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1, 1, 2])
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8])

    def test_edge_cases(self):
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        self.assertEqual(fibonacci_sequence(2), [0, 1, 1, 2])
        self.assertEqual(fibonacci_sequence(3), [0, 1, 1, 2, 3])

    def test_larger_numbers(self):
        self.assertEqual(fibonacci_sequence(21), [0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(fibonacci_sequence(50), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibonacci_sequence(100), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-10)
        with self.assertRaises(ValueError):
            fibonacci_sequence(-100)

    def test_input_validation(self):
        with self.assertRaises(TypeError):
            fibonacci_sequence(3.14)
        with self.assertRaises(TypeError):
            fibonacci_sequence("5")
        with self.assertRaises(TypeError):
            fibonacci_sequence(None)


if __name__ == '__main__':
    unittest.main()