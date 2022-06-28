from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        d=Counter(s)
        delete=0
        s=set()
        for i,j in d.items():
            while j >0 and j in s:
                j-=1
                delete+=1
            s.add(j)
        return delete
        
        
            
        
        