from typing import List

class Solution:
    def searchIterative(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + (right - left)) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return -1
    
    def searchRecursive(self, nums, target, left, right):
        if left > right:
            return -1
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.searchRecursive(nums, target, mid + 1, right)
        else:
            return self.searchRecursive(nums, target, left, mid - 1)

if __name__ == '__main__':
    self = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    self.searchRecursive(nums, target, 0, len(nums) - 1)
    