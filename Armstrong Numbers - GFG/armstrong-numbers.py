#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        temp=n
        s=0
        while temp!=0:
            t=temp%10
            s=s+pow(t,3)
            temp=temp//10
        return "Yes" if s==n else "No"
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends