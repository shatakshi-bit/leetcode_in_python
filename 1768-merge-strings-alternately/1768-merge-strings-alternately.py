class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=min(len(word1),len(word2))
        i=0
        l=[]
        while i<m:
            l.append(word1[i])
            l.append(word2[i])
            i+=1
        if len(word1)>len(word2):
            l.append(word1[i:])
        else:
            l.append(word2[i:])
            
        return "".join(l)
            
            
            
            
        
        
        