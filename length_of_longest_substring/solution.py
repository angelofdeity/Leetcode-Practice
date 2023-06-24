class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = {}
        offset = longest = 0
        for i in range(len(s)):
            char = s[i]
            if char in indexes and indexes[char] >= offset:
                window = i - offset
                offset = indexes[char] + 1  # found a repeat
                longest = max(window, longest)
            indexes[char] = i
        return max(longest, (len(s) - offset))


s = "abbbcdde"
