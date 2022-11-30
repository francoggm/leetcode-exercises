from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[len(nums) - k%len(nums):] + nums[:len(nums) - k%len(nums)]
        # [nums.insert(0, nums.pop(-1)) for _ in range(k)]
        print(nums)

if __name__ == '__main__':
    self = Solution()
    self.rotate([-1,-100,3,99], 2)
    
    
    k = 2
    n = len([1,2,3,4,5,6,7, 10]) 
    k % n
    a = [1,2,3, 5, 6]

    a[:] = a[-2:] + a[:2+1]

    5 % 2 
