class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length=high-low+1
        count=length//2
        if length%2!=0 and low%2!=0:
            return count+1
        return count

        
        
        