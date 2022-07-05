class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        s = set(nums)
        ans=0
        n=len(nums)
        
        for i in range(len(nums)):
            
            # current element is starting point
            if (nums[i]-1) not in s:
                
                # Then check for next elements in the sequence
                j = nums[i]
                while(j in s):
                    j += 1

                maxLength = max(maxLength, j-nums[i])
        return maxLength
           
        