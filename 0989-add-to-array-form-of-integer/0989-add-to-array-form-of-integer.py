class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        strr=""
        for i in num:
            strr=strr+str(i)
        s=str(int(strr)+k)
        ans=[]
        for i in s:
            ans.append(int(i))
        return ans
        
            
         