#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        temp=N
        c=0
        while temp!=0:
            t=temp%10
            if t!=0 and N%t==0:
            # print(t)
                c=c+1
            temp=temp//10
        return c
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends