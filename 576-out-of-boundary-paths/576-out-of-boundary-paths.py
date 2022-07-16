class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7
        self.directions = [[0,-1],[0,1],[1,0],[-1,0]]
        
        @lru_cache(maxsize = None)
        def dfs(r,c,moves):
            default = 0
            for dr,dc in self.directions:
                nr,nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    if moves > 0:
                        default = (default + 1) % mod
                    continue
                if moves > 1:
                    default = (default + dfs(nr,nc,moves-1)) % mod
            return default
        return dfs(startRow,startColumn,maxMove) % mod
        