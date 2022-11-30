
def isSubsequence(s, t):
    if (len(s) >= 0 and len(s) <= 100) and (len(t) >= 0 and len(t) <= (10**4)):
        pointer = 0
        for i in range(len(s)):
            for j, y in enumerate(t):
                if s[i] == y:
                    pointer += 1
                    t = t[j+1:]
                    break
            if pointer == len(s):
                return True
    return False

s = 'abc'
t = 'ahbgdc'

isSubsequence(s, t)            


