class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        d = m*n
        ans = [[0] * n for _ in range(m)]
        
        start = d - k
        for i in range(m):
            for j in range(n):
                start %= d
                r = start // n
                c = start % n
                ans[i][j] = grid[r][c]
                start += 1
        return ans
        