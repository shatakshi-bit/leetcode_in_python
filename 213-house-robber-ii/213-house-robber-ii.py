class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(arr):
            n=len(arr)
            prev=arr[0]
            prev2=0
            for i in range(1,n):
                take=arr[i]
                if i>1:
                    take+=prev2
                nottake=0+prev
                curi=max(take,nottake)
                prev2=prev
                prev=curi
            return prev 
        if len(nums)==1:
            return nums[0]
        return max(f(nums[1:len(nums)]),f(nums[:-1]))
        
        