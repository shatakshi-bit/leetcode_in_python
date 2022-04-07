class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            stones.sort()
            l=len(stones)
            if stones[l-1]==stones[l-2]:
                stones.pop()
                stones.pop()
            else:
                s,t=stones[l-1],stones[l-2]
                stones.pop()
                stones.pop()
                stones.append(abs(s-t))
        if len(stones)!=0:
            return stones[0]
        else:
            return 0
    
            

            
            
        
        