class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        s=[]
        for i,j in sorted(d.items(), key=lambda a: a[1], reverse=True):
            s.append(i)
            k=k-1
            if k==0:
                break
        return s
        
            
            
            
        
        
            
        