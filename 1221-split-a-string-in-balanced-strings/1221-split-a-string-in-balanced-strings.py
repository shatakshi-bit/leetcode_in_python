class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c,cr=0,0
        for i in s:
            if  i=='R':
                cr=cr+1
            else:
                cr=cr-1
            if cr==0:
                c=c+1
        return c
            
            
        