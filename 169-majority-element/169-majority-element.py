from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        count=Counter(nums)
        for i in count.keys():
            if count[i]>(len(nums)//2):
                return i
     
        