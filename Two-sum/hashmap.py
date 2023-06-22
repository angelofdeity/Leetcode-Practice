class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i

sol1 = Solution()
print(sol1.twoSum([2,2,2,2], 4))
