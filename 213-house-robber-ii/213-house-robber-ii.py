class Solution:
    def f(self,nums):
            n=len(nums)
            prev=nums[0]
            prev2=0
            for i in range(1,n):
                take=nums[i]
                if i>1:
                    take+=prev2
                nottake=0+prev
                curi=max(take,nottake)
                prev2=prev
                prev=curi
            return prev 
    def rob(self, nums: List[int]) -> int:
        # def f(arr):
        #     n=len(arr)
        #     prev=nums[0]
        #     prev2=0
        #     for i in range(1,n):
        #         take=nums[i]
        #         if i>1:
        #             take+=prev2
        #         nottake=0+prev
        #         curi=max(take,nottake)
        #         prev2=prev
        #         prev=curi
        #     return prev 
        if len(nums)==1:
            return nums[0]
        # print(nums[1:len(nums)],nums[:len(nums)-1])
        # print(f(nums[1:len(nums)]),f(nums[:len(nums)-1]))
        return max(self.f(nums[1:len(nums)]),self.f(nums[:-1]))
        
        