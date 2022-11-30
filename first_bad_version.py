class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1