#!/usr/bin/python3
def get_two_sum(target, nums):
  n = len(nums)
  for i in range(n - 1):
    j = i + 1
    for j in range(n):
      if nums[i] + nums[j] == target:
        return [i, j]

sum = get_two_sum(20, [3, 4, 6, 8, 20])
print(sum)
