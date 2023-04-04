class Solution:
    def partitionString(self, s: str) -> int:
        #TC-->O(n),SC-->O(1)
        x=set()
        res=1
        for i in s:
            if i in x:
                res+=1
                x=set()
            x.add(i)
        return res
        