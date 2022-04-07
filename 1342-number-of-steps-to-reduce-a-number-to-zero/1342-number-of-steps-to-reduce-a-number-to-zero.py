class Solution:
    def numberOfSteps(self, num: int) -> int:
        c=0
        while num:
            if (num & 1)==0:
                num=num>>1
            else:
                num-=1
            c+=1
        return c
        
        