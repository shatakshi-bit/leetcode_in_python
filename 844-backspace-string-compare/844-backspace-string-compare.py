class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def abc(ST):
            ans=[]
            for c in ST:
                if c!="#":
                    ans.append(c)
                else:
                    if len(ans)!=0:
                        ans.pop()
            return "".join(ans)
        return abc(s)==abc(t)

    
        
        
        