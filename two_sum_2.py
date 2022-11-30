from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i, j in enumerate(numbers):
        #     find = target - j
        #     left = i + 1
        #     right = len(numbers) - 1
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         if numbers[mid] == find:
        #             return[i + 1, mid + 1]
        #         elif numbers[mid] < find:
        #             left = mid + 1
        #         elif numbers[mid] > find:
        #             right = mid - 1
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1                
            

if __name__ == '__main__':
    self = Solution()
    self.twoSum([2,7,11,15], 9)       