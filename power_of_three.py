class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        while n > 1:
            n /= 3
            print(n)
            if n == 1:
                return True
            elif not n.is_integer():
                break
        return False
    
    def isPowerOfThree_2(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        powers = [3**x for x in range(31)]
        return True if n in powers else False

if __name__ == '__main__':
    self = Solution()
    self.isPowerOfThree_2(81)

    n = 27

         