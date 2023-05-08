class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        #TC-->O(n^2) SC-->O(1)
        # r,c=len(mat),len(mat[0])
        # ld,rd=0,0
        # for i in range(r):
        #     for j in range(c):
        #         if i==j:
        #             ld=ld+mat[i][j]
        #         elif i!=j and (i+j)==r-1:
        #             rd=rd+mat[i][j]
        # return (ld+rd)
        
        n=len(mat)
        res=0
        for i in range(n):
            res+=mat[i][i]
            res+=mat[i][n-1-i]
        return (res-mat[n//2][n//2]) if n%2!=0 else res
    
                
                
                
        
        