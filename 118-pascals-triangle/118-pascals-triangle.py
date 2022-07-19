class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l1=[[1],[1,1]]
        ro=len(l1)
        #numRows=5
        #print(row)
        if numRows==1:
            return [l1[0]]
        elif numRows==2:
            return l1
        else:
            for  r in range(2,numRows):
                l2=[]
                for c in range(r+1):
                            if c==0 or c==r:
                                l2.append(1)
                                #print(l2)
                            else:
                                l2.append(l1[r-1][c-1]+l1[r-1][c])
                                #print(l2)
                l1.append(l2)
            return l1
        