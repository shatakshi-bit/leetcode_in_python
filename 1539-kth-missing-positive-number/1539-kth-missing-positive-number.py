class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        m=arr[len(arr)-1]
        x=[]
        for i in range(1,m+k+1):
            if i not in arr:
                x.append(i)
        return x[k-1]
            
                
        