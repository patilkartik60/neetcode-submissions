class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        check = {}
        for i in range(len(s)):
            check[s[i]] = 1 + check.get(s[i], 0)

        for j in range(len(t)):
            if t[j] in check:
                check[t[j]] -= 1
                if check[t[j]] == 0:
                    del check[t[j]]
        
        if not check:
            return True
        
        return False

        