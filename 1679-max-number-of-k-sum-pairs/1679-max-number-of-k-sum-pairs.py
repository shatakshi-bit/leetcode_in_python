class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        o=0
        c=Counter(nums)
        #print(c)
        seen=set()
        for i in c:
            if i==(k-i):
                o+=c[i]//2
            else:
                if i not in seen and (k-i) in c:
                    o+=min(c[i],c[k-i])
            seen.add(i)
            seen.add(k-i)
        return o
                
            
        
        