class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        
        def dfs(r,c):
            if (r<0 or r==ROWS or c<0 or c==COLS or grid[r][c]==0 or (r,c) in visit):
                return 0
            visit.add((r,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))
        area=0
        for r in range(ROWS):
            for c in range(COLS):
                area=max(area,dfs(r,c))
        return area
        
        
        # def dfs(i,j):
        #     if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
        #         return 0
        #     grid[i][j]=0
        #     down = dfs(i+1,j)
        #     up = dfs(i-1,j)
        #     right = dfs(i,j+1)
        #     left = dfs(i,j-1)
        #     a = 1+(up+down+right+left)
        #     return a
        # ans = 0
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         ans = max(ans,dfs(row,col))
        # return ans