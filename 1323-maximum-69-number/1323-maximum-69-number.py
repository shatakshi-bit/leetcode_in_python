class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        c=1
        t=""
        for i in s:
            if i=='6' and c==1:
                t=t+'9'
                c=c-1
            else:
                t=t+i
        return t
            
                
        