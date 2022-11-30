class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        while x <= n:
            if x != n:
                x = x * 4
            else:
                return True
        return False


if __name__ == '__main__':
    self = Solution()
    self.isPowerOfFour(177884)


