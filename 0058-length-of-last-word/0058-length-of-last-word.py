class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=" ":
                c=c+1
            else:
                break
        return c
        