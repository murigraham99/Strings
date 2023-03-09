import unittest
import strings

class TestStrings(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(strings.is_palindrome("kayak"), "palindrome")
        self.assertEqual(strings.is_palindrome("test"), "not palindrome")
        self.assertEqual(strings.is_palindrome("k"), "palindrome")

    def test_longest_word(self):
        self.assertEqual(strings.longest_word("This is a test"), "This")
        self.assertEqual(strings.longest_word("test"), "test")

    def test_anagrams(self):
        self.assertEqual(strings.anagrams("ana", "naa"), "YES")
        self.assertEqual(strings.anagrams("anb", "naa"), "NO")
        self.assertEqual(strings.anagrams("a", "a"), "YES")

    def test_reverse_string(self):
        self.assertEqual(strings.reverse_string("test"), "tset")
        self.assertEqual(strings.reverse_string("000"), "000")

    def test_most_common_word(self):
        self.assertEqual(strings.most_common_word("This is a test this"), "This")
        self.assertEqual(strings.most_common_word("test"), "test")

    def test_password_generator(self):
        self.assertEqual(len(strings.password_generator(10)), 10)



