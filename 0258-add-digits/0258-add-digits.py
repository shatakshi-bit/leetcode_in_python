class Solution:
    def addDigits(self, num: int) -> int:
        # while num > 9:
        #     num = num % 10 + num // 10
        # return num
        if num==0:
            return 0
        if num%9==0:
            return 9
        else:
            return num%9
    
        
        
        
        