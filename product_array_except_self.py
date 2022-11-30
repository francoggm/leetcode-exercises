from typing import List

nums = [1,2,3,4]

class Solution:
    #Time Limit
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            product = 1
            new_list = nums[:i] + nums[i+1:]
            for j in range(len(new_list)):
                product *= new_list[j]
            products.append(product)

class Solution:
    #Time Limit
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        n = len(nums)
        while len(products) < n:
            product = 1
            for i in range(n):
                if i != len(products):
                    product *= nums[i]
            products.append(product)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, products, prefix, suffix = len(nums), [1] * len(nums), 1, 1
        for i in range(n):
            products[i] = prefix 
            prefix *= nums[i]
        for i in range(n -1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]
            
            
        

