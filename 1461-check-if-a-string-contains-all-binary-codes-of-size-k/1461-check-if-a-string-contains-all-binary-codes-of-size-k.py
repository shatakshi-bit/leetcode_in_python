class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        countset=set()
        for i in range(len(s)-k+1):
            countset.add(s[i:i+k])
        return len(countset)==2**k
        
        