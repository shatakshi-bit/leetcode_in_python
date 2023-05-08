class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r,c=len(mat),len(mat[0])
        ld,rd=0,0
        for i in range(r):
            for j in range(c):
                if i==j:
                    ld=ld+mat[i][j]
                elif i!=j and (i+j)==r-1:
                    rd=rd+mat[i][j]
        return (ld+rd)
                
                
                
        
        