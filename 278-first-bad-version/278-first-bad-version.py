# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        s, e = 0, n
        bad = math.inf
        while s <= e:
            m = (s+e)//2
            if isBadVersion(m):
                bad = min(bad, m)
                e = m-1 
            else:
                s = m+1
        return bad
        