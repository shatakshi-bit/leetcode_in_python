class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x=-x
            s=-1
        else:
            s=1
        ans=0
        while x!=0:
            t=x%10
            ans=ans*10+t
            x=x//10
        return 0 if ans>pow(2,31) else s*ans
            
        
            
            
            
    
            
        
        