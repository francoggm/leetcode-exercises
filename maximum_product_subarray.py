from typing import List

nums = [2,3,-2,4]

nums = [-2,0,-1]
nums = [6,-4, -3]
nums = [-2]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = float('-inf')
        for i in range(n - 1):
            count = nums[i]
            for j in range(i + 1, n):
                max_count = max(max_count, count)
                count *= nums[j]

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            res = max(res, curMax, curMin)
        return res


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            if n < 0:
                curMin, curMax = curMax, curMin

            curMax = max(n, curMax * n)
            curMin = min(n, curMin * n)

            res = max(res, curMax)
        return res

            
            