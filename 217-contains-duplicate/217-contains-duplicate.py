from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        f=0
        mydict=Counter(nums)
        for i in mydict.values():
            if i>1:
                f=1
        if f==1:
            return True
        else:
            return False

        
        
        
        
        