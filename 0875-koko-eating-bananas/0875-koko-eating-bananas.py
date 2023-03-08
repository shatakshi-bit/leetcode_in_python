class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bananas(piles,k,h):
            hours=0
            for i in piles:
                div=i//k
                hours+=div
                if (i%k)!=0:
                    hours+=1
            return hours<=h
        l=1
        r=max(piles)
        while l<=r:
            m=l+(r-l)//2
            if (bananas(piles,m,h)):
                r=m-1
            else:
                l=m+1
        return l
                
            
        