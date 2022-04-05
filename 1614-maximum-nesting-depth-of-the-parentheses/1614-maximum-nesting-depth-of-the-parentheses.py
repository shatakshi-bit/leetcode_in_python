class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        depth,ans=0,0
        for i in s:
            if i=='(':
                stack.append(i)
                depth+=1
                ans=max(depth,ans)
            elif i==")":
                stack.pop()
                depth-=1
        if len(stack)==0:
            return ans
        