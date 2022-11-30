from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, j in enumerate(nums):
            for k, z in enumerate(nums[i+1:]):
                if z + j == target:
                    k += 1
                    return [i, k + i]

   


