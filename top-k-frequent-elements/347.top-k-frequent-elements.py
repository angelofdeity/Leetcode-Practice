#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
from collections import Counter
# input - nums = [1, 2, 1, 1, 3, 4, 4, 4, 2]; k = 3
# hmap = {1: 3,
#         2: 2,
#         3: 1,
#         4: 3}

#         0   1    2     3
# freq = [0, [3], [2], [1, 4]]
# expected output - [4, 1, 2]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[]] * (len(nums) + 1)  # Generate array bucket
        hmap = Counter(nums)  # count and index nums
        for key, val in hmap.items():
            if not freq[val]:
                freq[val] = [key]
            else:
                freq[val].append(key)
        res = []
        # Get the top k frequent elements
        # loop backwards through array bucket
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                k -= 1
                if not k:
                    return res
        return res


# @lc code=end
