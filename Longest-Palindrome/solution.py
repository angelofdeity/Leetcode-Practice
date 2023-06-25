class Solution:
    def longest_palindrome(self, s: str) -> str:
        indexes = {}
        offset = 0
        max_length = 1
        for i in range(len(s)):
            char = s[i]
            if char in indexes:
                offset = indexes[char]
                if result := self.is_palindrome(s[offset:i + 1]):
                    print(result)
                    length = len(result)
                    max_length = max(length, max_length)
            indexes[char] = i
        return s[offset:offset + max_length]

    def is_palindrome(self, s):
        j = len(s) - 1
        for i in range(len(s)):
            if i == j:
                break
            if (s[i] != s[j]):
                return None
            j -= 1
        return s


print(Solution().longest_palindrome('babababab'))
