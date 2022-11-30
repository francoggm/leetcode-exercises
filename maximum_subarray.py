from typing import List

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
nums = [-2,-1]
nums = [-2,-3,-1]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Time limit
        n = len(nums)
        if n < 2:
            return sum(nums)
        max_sum = float('-inf')
        for i in range(n):
            summ = nums[i]
            if max_sum < summ:
                max_sum = summ
            for j in range(i + 1, n):
                summ += nums[j]
                if max_sum < summ:
                        max_sum = summ
        return max_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Time limit
        right = len(nums)
        left = 0
        max_sum = sum(nums)

        if right <= 1:
            return max_sum

        while right > left:
            print(nums[left:right])
            print(nums[left:right-1])
            print(nums[left+1:right])

            if max_sum < sum(nums[left:right]):
                max_sum = sum(nums[left:right])

            if max_sum < sum(nums[left:right-1]):
                max_sum = sum(nums[left:right-1])

            if max_sum < sum(nums[left+1:right]):
                max_sum = sum(nums[left+1:right])
            right -= 1
            left += 1
        return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [[0] * len(nums) for i in range(2)]
        dp[0][0], dp[1][0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            dp[1][i] = max(nums[i], nums[i] + dp[1][i-1])
            dp[0][i] = max(dp[0][i-1], dp[1][i])
        return dp[0][-1]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        return max(dp)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(nums[i], nums[i] + dp[i-1]))
        return max(dp)

class Solution:
    #Melhor
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(maxSub, curSum)
        return maxSub
        

  
