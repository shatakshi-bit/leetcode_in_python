class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # strr=""
        # for i in num:
        #     strr=strr+str(i)
        # s=str(int(strr)+k)
        # ans=[]
        # for i in s:
        #     ans.append(int(i))
        # return ans
        
        num.reverse()
        i=0
        while k:
            digit=k%10
            if i<len(num):
                num[i]+=digit
            else:
                num.append(digit)
            
            carry=num[i]//10
            num[i]=num[i]%10
            
            k=k//10
            k+=carry
            i=i+1
            
        return num[::-1]
        
            
         