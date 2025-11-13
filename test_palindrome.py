import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_basic_palindromes(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("aba"))
        self.assertTrue(is_palindrome("abba"))
        self.assertTrue(is_palindrome("racecar"))

    def test_mixed_characters_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Madam, I'm Adam"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("a1!1a"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("programming"))
        self.assertFalse(is_palindrome("12345"))
        self.assertFalse(is_palindrome("abc123"))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome("Aa"))
        self.assertFalse(is_palindrome("ab"))

    def test_input_validation(self):
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(None)
        with self.assertRaises(TypeError):
            is_palindrome([1, 2, 3])


if __name__ == '__main__':
    unittest.main()