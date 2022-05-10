class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a=Counter(s)
        b=Counter(t)
        for i in set(s):
            if a[i]!=b[i]:
                return False
        return True
                
        