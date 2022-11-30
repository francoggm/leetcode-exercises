from typing import List

nums= [1,2,3,1]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict = {}
        for i in range(len(nums)):
            duplicate_dict.setdefault(nums[i], 0)
            duplicate_dict[nums[i]] += 1
            if duplicate_dict[nums[i]] > 1:
                return True
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                    return True
        return False

class Solution:
    #Melhor
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False