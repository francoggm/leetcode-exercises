class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            if  len(s) >= 1 and len(s) <= 5 * (10**4):
                words_dict = {}
                for i in range(len(s)):
                    if not s[i] in words_dict and t[i] not in words_dict.values():
                        words_dict[s[i]] = t[i]
                new_string = ''
                for y in s:
                    if y in words_dict:
                        new_string += words_dict[y]
                if new_string == t: return True
        return False


self = Solution()
self.isIsomorphic('egg', 'add')


