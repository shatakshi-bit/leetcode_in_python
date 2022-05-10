class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o=[]
        for j in range(len(nums)-1):
            for i in range(j+1,len(nums)):
                 if (nums[j]+nums[i])==target:
                        o.append(j)
                        o.append(i)
        return o
                        
                
        