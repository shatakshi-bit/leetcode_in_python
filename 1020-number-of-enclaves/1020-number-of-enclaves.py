class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visit=set()
        
        def dfs(r,c):
            if r<0 or r==row or c<0 or c==col or not grid[r][c] or (r,c) in visit:
                return 0
            res=1
            visit.add((r,c))
            for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                res+=dfs(r+dr,c+dc)
            return res
                
            
            
                
        land,borderland=0,0    
        for r in range(row):
            for c in range(col):
                land+=grid[r][c]
                if (grid[r][c] and (r,c) not in visit) and (r in [0,row-1] or c in [0,col-1]):
                    borderland+=dfs(r,c)
        return land-borderland
        
        