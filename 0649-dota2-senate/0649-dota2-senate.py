class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R,D=deque(),deque()
        l=len(senate)
        for i,j in enumerate(senate):
            if j=="R":
                R.append(i)
            else:
                D.append(i)
        while R and D:
            r=R.popleft()
            d=D.popleft()
            
            if r<d:
                R.append(r+l)
            else:
                D.append(d+l)
        return "Radiant" if R else "Dire"
                
        