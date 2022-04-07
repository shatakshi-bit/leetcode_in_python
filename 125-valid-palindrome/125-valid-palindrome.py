class Solution:
    def isPalindrome(self, s: str) -> bool:
        # listt=list(s)
        # ns,nt="",""
        # l=len(listt)
        # for i in range(l):
        #     if listt[l-i-1].isalnum():
        #         ns=ns+listt[l-i-1].lower()
        #     # if listt[i].isalnum():
        #     #     nt=nt+listt[i].lower()
        # # print(ns)
        # # print(nt)
        # if ns==ns[::-1]:
        #     return True
        # else:
        #     return False
        alpha='qwertyuiopasdfghjklzxcvbnm1234567890'
        new=''
        # converting to lowercase
        s=s.lower()
        
        # fetching the ascii characters
        for i in range(len(s)):
            if s[i] in alpha:
                
                new=new+s[i]
        
        return new==new[::-1]
                
                
            
        