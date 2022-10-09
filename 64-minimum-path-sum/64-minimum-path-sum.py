class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
#         #recursion
#         m,n=len(grid),len(grid[0])
#         def f(i,j):
#             if i==0 and j==0:
#                 return grid[i][j]
#             if i<0 or j<0:
#                 return 1e9
#             up=grid[i][j]+f(i-1,j)
#             left=grid[i][j]+f(i,j-1)
#             return min(left,up)
#         return f(m-1,n-1)
    
#         #memoization
#         m,n=len(grid),len(grid[0])
#         dp=[[-1]*n for i in range(m)]
#         m,n=len(grid),len(grid[0])
#         def f(i,j,dp):
#             if i==0 and j==0:
#                 return grid[i][j]
#             if i<0 or j<0:
#                 return 1e9
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             up=grid[i][j]+f(i-1,j,dp)
#             left=grid[i][j]+f(i,j-1,dp)
#             dp[i][j]=min(left,up)
#             return dp[i][j]
#         return f(m-1,n-1,dp)
    
        #tabulation
        m,n=len(grid),len(grid[0])
        dp=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    up=grid[i][j]
                    if i>0:
                        up+=dp[i-1][j]
                    else:
                        up+=1e9
                    left=grid[i][j]
                    if j>0:
                        left+=dp[i][j-1]
                    else:
                        left+=1e9
                    dp[i][j]=min(up,left)    
        return dp[m-1][n-1]
                    
                