class Solution:
    def maxProduct(self, words: List[str]) -> int:
        marks=[]
        for word in words:
            mask=0
            for c in word:
                bit=ord(c)-ord('a')
                mask|=1<<bit
            marks.append(mask)
        ans=0
        n=len(words)
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if marks[i] & marks[j]==0:
                        ans=max(ans,len(words[i])*len(words[j]))
        return ans
    
        
        