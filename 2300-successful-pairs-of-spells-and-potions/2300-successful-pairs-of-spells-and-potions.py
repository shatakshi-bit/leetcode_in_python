class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        
        for i in spells:
            l,r=0,len(potions)-1
            idx=len(potions)
            while l<=r:
                m=(l+r)//2
                if i*potions[m]>=success:
                    r=m-1
                    idx=m
                else:
                    l=m+1
            res.append(len(potions)-idx)
        return res
                    

        
        # res=[]
        # for i in range(len(spells)):
        #     c=0
        #     for j in range(len(potions)):
        #         if spells[i]*potions[j]>=success:
        #             c=c+1
        #     res.append(c)
        # return res
        