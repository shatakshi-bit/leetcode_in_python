class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        num=sorted(nums)
        N=len(nums)
        l,r,c=N,0,0
        for i,n in enumerate(nums):
            if nums[i]!=num[i]:
                c=1
                l=min(i,l)
                r=max(i,r)
        if l==r or c==0:
            return 0
        else:
             return r-l+1
                
                
        
        
        
        
        
        
        
        