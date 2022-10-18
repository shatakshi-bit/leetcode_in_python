class Solution:
    def canPartition(self, nums: List[int]) -> bool:
            s=sum(nums)
            n=len(nums)
            if s%2:
                return False
            k=s//2
            dp=[[0 for j in range(k+1)] for i in range(n)]
            for i in range(n):
                dp[i][0]=True
            if nums[0]<=k:
                dp[0][nums[0]]=True
            for ind in range(1,n):
                for target in range(1,k+1):
                    nottake=dp[ind-1][target]
                    take=False
                    if nums[ind]<=target:
                        take=dp[ind-1][target-nums[ind]]
                    dp[ind][target]=(take or nottake)
            return dp[n-1][k]
    
         
    
        # def f(ind,target,dp):
        #     if target==0:
        #         return True
        #     if ind==0:
        #         return nums[0]==target
        #     if dp[ind][target]!=-1:
        #         return dp[ind][target]
        #     nottake=f(ind-1,target,dp)
        #     take=False
        #     if nums[ind]<=target:
        #         take=f(ind-1,target-nums[ind],dp)
        #     dp[ind][target]=(take or nottake)
        #     return dp[ind][target]
        # s=sum(nums)
        # if s%2:
        #     return False
        # target=s//2
        # dp=[[-1 for j in range(target+1)] for i in range(len(nums))]    
        # return f(len(nums)-1,target,dp)
        
        