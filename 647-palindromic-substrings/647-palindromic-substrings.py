class Solution:
    def countSubstrings(self, s: str) -> int:
        lst =  []
        n = len(s)
        for i in range(n):
            lst.append(s[i])
        
        cnt = 0
        for i in range(n):
            for j in range(n-i-1):
                
                lst[j] += s[i+j+1]
                if lst[j]==lst[j][::-1]:
                    cnt+=1
        return cnt+n
        