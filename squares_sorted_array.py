from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([(x) ** 2 for x in nums])

if __name__ == '__main__':
    self = Solution()
    self.sortedSquares([-7,-3,2,3,11])