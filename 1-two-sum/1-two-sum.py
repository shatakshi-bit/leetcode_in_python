class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        li=[]
        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    #print(nums[i],nums[j])
                    li.append(i)
                    li.append(j)
        return li
        
                    
            
        