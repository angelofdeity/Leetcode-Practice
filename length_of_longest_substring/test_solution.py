import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lengthOfLongestSubstring_emptyString(self):
        # Test with an empty string
        s = ""
        expected = 0
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_allUniqueCharacters(self):
        # Test with a string containing all unique characters
        s = "abcdefg"
        expected = 7
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_repeatingCharacters(self):
        # Test with a string containing repeating characters
        s = "aabccdefg"
        expected = 5
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_longestAtEnd(self):
        # Test with the longest substring at the end of the string
        s = "abcdefgabc"
        expected = 7
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_longestAtStart(self):
        # Test with the longest substring at the start of the string
        s = "abcabcdefg"
        expected = 7
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_longestInMiddle(self):
        # Test with the longest substring in the middle of the string
        s = "abcabcdefgabc"
        expected = 7
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)
    def test_lengthOfLongestSubstring_noRepeatingCharacters(self):
        # Test with a string containing no repeating characters
        s = "abcdefg"
        expected = 7
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_singleCharacter(self):
        # Test with a string containing a single character
        s = "dvdf"
        expected = 3
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_allRepeatingCharacters(self):
        # Test with a string containing all repeating characters
        s = "aaaaa"
        expected = 1
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_mixedCharacters(self):
        # Test with a string containing a mix of repeating and non-repeating characters
        s = "abbbcdde"
        expected = 3
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_unicodeCharacters(self):
        # Test with a string containing Unicode characters
        s = "🌟⭐️🌟⭐️"
        expected = 3
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()

