class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s=1
        for i in nums:
            s=s*i
        if s<0:
            return -1
        elif s>0:
            return 1
        else:
            return 0
            
        