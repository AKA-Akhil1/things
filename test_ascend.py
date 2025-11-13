import unittest
from ascend import sort_ascending


class TestSortAscending(unittest.TestCase):
    def test_basic_sorting(self):
        self.assertEqual(sort_ascending([3, 1, 4, 2]), [1, 2, 3, 4])
        self.assertEqual(sort_ascending([5, 2, 8, 1, 9]), [1, 2, 5, 8, 9])
        self.assertEqual(sort_ascending([10, 5, 15]), [5, 10, 15])

    def test_different_list_sizes(self):
        self.assertEqual(sort_ascending([]), [])
        self.assertEqual(sort_ascending([42]), [42])
        self.assertEqual(sort_ascending([3, 1]), [1, 3])
        self.assertEqual(sort_ascending([7, 2, 9, 1, 5, 3, 8, 6, 4]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_repeated_elements(self):
        self.assertEqual(sort_ascending([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3])
        self.assertEqual(sort_ascending([5, 5, 5, 5]), [5, 5, 5, 5])
        self.assertEqual(sort_ascending([2, 1, 2, 3, 1, 3]), [1, 1, 2, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(sort_ascending([-1, -3, -2]), [-3, -2, -1])
        self.assertEqual(sort_ascending([3, -1, 0, -2, 1]), [-2, -1, 0, 1, 3])
        self.assertEqual(sort_ascending([-5, -5, -1, -3]), [-5, -5, -3, -1])

    def test_input_validation(self):
        with self.assertRaises(TypeError):
            sort_ascending("not a list")
        with self.assertRaises(ValueError):
            sort_ascending([1, 2, "3"])
        with self.assertRaises(ValueError):
            sort_ascending([1, 2.5, 3])


if __name__ == '__main__':
    unittest.main()