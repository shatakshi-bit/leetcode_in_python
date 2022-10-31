#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        t1 = A
        t2 = B
        while t1 != t2:
            if t1 > t2:
                t1 -= t2
            else:
                t2 -= t1
        gcd = t1
        lcm = A * B // gcd
        return [lcm, gcd]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends