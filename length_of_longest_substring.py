class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = 0
        group = []
        for char in s:
            if char in group:
                longest_sub = len(group) if len(group) > longest_sub else longest_sub
                group = []
            group.append(char)
        return longest_sub

print(Solution().lengthOfLongestSubstring(" "))
