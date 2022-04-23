from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            f=0
            x=Counter(s)
            y=Counter(t)
            for i in x.keys():
                c=0
                for j in y.keys():
                    if i==j:
                        c=1
                        if x[i]!=y[j]:
                            f=1
                if c==0:
                    return False
            if f==1:
                return False
            else:
                return True


                        
                    

                
            