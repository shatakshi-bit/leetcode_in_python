#User function Template for python3
import math
class Solution:
    def sumOfSeries(self,N):
        tot = N*(N+1)//2
        return pow(tot,2)
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
# } Driver Code Ends