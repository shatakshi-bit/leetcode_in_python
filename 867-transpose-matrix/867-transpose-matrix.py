class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result_m=[]
        for i in range(len(matrix[0])):
            m=[]
            for j in range(len(matrix)):
                m.append(matrix[j][i])
            result_m.append(m)
        return result_m
            
        