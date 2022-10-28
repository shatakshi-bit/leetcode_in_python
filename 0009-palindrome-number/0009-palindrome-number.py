class Solution:
    def isPalindrome(self, x: int) -> bool:
        f=0
        if x<0:
            return False
        temp=x
        s=0
        while temp:
            t=temp%10
            s=s*10+t
            temp=temp//10
        return True if s==x else False
        
        
        
        