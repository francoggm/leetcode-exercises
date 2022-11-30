from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zeroes = len([x for x in nums if x == 0])
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        # nums[:] += [0] * zeroes
        
        print(nums)


if __name__ == '__main__':
    self = Solution()
    self.moveZeroes([0,0,1])

    nums = [0,1,0,3,12]
    pos = 0
    for num in nums:
        if num != 0:
            nums[pos] = num
            pos += 1
    while(pos < len(nums)):
        nums[pos] = 0
        pos += 1