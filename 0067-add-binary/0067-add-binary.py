class Solution:
    def addBinary(self, a: str, b: str) -> str:
        alen=len(a)
        blen=len(b)
        i=0
        carry=0
        res=""
        
    
        while (i<alen or i<blen or carry!=0):
            x=0
            if i<alen and a[alen-i-1]=='1':
                x=1
            y=0
            if i<blen and b[blen-i-1]=='1':
                y=1
            res=str((x+y+carry)%2)+res
            carry=(x+y+carry)//2
            i+=1
        return res
            
            
            
         
        
        