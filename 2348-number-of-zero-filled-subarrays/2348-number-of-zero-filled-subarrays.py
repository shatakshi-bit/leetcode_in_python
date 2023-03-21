class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i,res,c=0,0,0
        while i<len(nums):
            if nums[i]==0:
                c+=1
                res+=c
            else:
                c=0
            i+=1
        return res
                
            
            
        