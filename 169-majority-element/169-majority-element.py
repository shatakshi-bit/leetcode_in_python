class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        d={}
        c=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j>(l//2):
                return i
            
        
            
        
        
    
    
            
            
        