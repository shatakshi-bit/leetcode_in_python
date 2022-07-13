class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        row, col = [0] * m, [0] * n
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[j] = 1
                    col[i] = 1
                    
        for i in range(len(row)):
            if row[i] == 1:
                for l in range(n):
                    matrix[l][i] = 0
        
        for i in range(len(col)):
            if col[i] == 1:
                for l in range(m):
                    matrix[i][l] = 0

        return matrix 