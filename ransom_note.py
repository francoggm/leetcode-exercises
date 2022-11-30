class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False

        for i in ransomNote:
            index = magazine.find(i)
            if index == -1:
                return False
            magazine = magazine.replace(i, '', 1)
        return True 

if __name__ == '__main__':
    self = Solution()
    self.canConstruct('a', 'b')

    