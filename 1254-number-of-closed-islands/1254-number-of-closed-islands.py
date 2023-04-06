class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visit=set()
        
        def dfs(i,j):
            if i<0 or j<0 or i==row or j==col:
                return 0
            if grid[i][j]==1 or (i,j) in visit:
                return 1
            
            visit.add((i,j))
            
            return min(dfs(i+1,j),
            dfs(i-1,j),
            dfs(i,j+1),
            dfs(i,j-1))
            
        res=0
        for i in range(row):
            for j in range(col):
                if not grid[i][j] and (i,j) not in visit:
                    res+=dfs(i,j)
        return res
        
                    
                    
            
            
        