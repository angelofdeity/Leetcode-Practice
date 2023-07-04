class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = {}
        offset = longest = 0
        for i in range(len(s)):
            char = s[i]
            if char in indexes and indexes[char] >= offset:
                offset = indexes[char] + 1  # found a repeat

            window = i - offset + 1
            indexes[char] = i
            longest = max(window, longest)
        return longest
