import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        for x,y in points:
            d=x**2 + y**2
            heap.append([d,x,y])
        heapq.heapify(heap)
        for i in range(k):
            dist,x,y=heapq.heappop(heap)
            ans.append([x,y])
        return ans
            
        
            
        