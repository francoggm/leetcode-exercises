from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            print(mid, left, right, nums[left:right+1])
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid 
            else:
                left = mid + 1
        print(mid, left, right)
        return left + 1 if nums[left] < target else left

if __name__ == '__main__':
    self = Solution()
    self.searchInsert([1,3,5,7], 6)
        