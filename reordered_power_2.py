class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        res = sorted([int(x) for x in str(n)])
        power_2 = [sorted([int(y) for y in str(2**x)]) for x in range(30)]
        return True if res in power_2 else False

if __name__ == '__main__':
    self = Solution()
    self.reorderedPowerOf2(64)
