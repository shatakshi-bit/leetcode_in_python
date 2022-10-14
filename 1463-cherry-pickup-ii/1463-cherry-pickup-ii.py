class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def f(i,j1,j2,dp):
            if j1<0 or j2<0 or j1>=c or j2>=c:
                return -1e9
            if i==r-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            if dp[i][j1][j2]!=-1:
                    return dp[i][j1][j2]
            maxi=-1e9
            for dj1 in range(-1,2):
                for dj2 in range(-1,2):
                    if j1==j2:
                        val=grid[i][j1]
                    else:
                        val=grid[i][j1]+grid[i][j2]
                    val+=f(i+1,j1+dj1,j2+dj2,dp)
                    maxi=max(maxi,val)
            dp[i][j1][j2]=maxi
            return dp[i][j1][j2]
        dp=[[[-1 for k in range(c)] for j in range(c)] for i in range(r)]
        return f(0,0,c-1,dp)
            
