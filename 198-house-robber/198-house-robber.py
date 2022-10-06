class Solution:
    def rob(self, nums: List[int]) -> int:
        #memoization
#         n=len(nums)-1
#         def f(i,dp):
#             if i==0:
#                 return nums[i]
#             if i<0:
#                 return 0
#             if dp[i]!=-1:
#                 return dp[i]
#             pick=nums[i]+f(i-2,dp)
#             notpick=0+f(i-1,dp)
#             dp[i]=max(pick,notpick)
#             return dp[i]
#         dp=[-1]*(len(nums)+1)
#         return f(n,dp)
    
         # #using Tabulation
        # if len(nums)==0:
        #     return 0
        # if len(nums)<=2:
        #     return max(nums)
        # dp=[0]*len(nums)
        # dp[1]=max(nums[0],nums[1])
        # dp[0]=nums[0]
        # for i in range(2,len(nums)):
        #     dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        # return dp[-1]
        
        # prev=0
        # cur=0
        # for num in nums:
        #     temp=prev
        #     prev=cur
        #     cur=max(num+temp,prev)
        # return cur
        
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
        
    
       
    
    

        
        
        
       



        
        