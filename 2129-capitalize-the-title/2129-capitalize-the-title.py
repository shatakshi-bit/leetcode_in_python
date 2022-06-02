class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=list(title.split(' '))
        #print(l)
        for i in range(len(l)):
            if len(l[i])>2:
                l[i]=l[i][0].upper()+l[i][1:len(l[i])].lower()
            else:
                l[i]=l[i][0:len(l[i])].lower()
        return " ".join(l)
                
       
            
        