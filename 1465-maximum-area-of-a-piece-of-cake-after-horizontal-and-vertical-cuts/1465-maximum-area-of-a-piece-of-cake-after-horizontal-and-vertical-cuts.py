class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalcuts=[0]+ horizontalCuts+[h]
        verticalCuts=[0]+verticalCuts+[w]
        max_h,max_v=0,0
        for i in range(1,len(horizontalcuts)):
            max_h=max(max_h,abs(horizontalcuts[i-1]-horizontalcuts[i]))
        for i in range(1,len(verticalCuts)):
            max_v=max(max_v,abs(verticalCuts[i-1]-verticalCuts[i]))
        return (max_h*max_v)%(10**9 + 7)
         
        
        
        