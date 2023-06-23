class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pair = {}
        w_start = 0
        for i in range(len(s)):
            old_index = pair[s[i]]
            if s[i] in pair and old_index >= w_start:
                w_start = old_index
                window = i - w_start
            else:
                pair[s[i]] = i
         return window
string = "abcabcdefgabc"
expected = 7, output = 7
string = "dkjvdfhju"
expected = 6, output = 5
print(Solution().lengthOfLongestSubstring(string))
