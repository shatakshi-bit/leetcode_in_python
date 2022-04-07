class Solution:
    def isPalindrome(self, s: str) -> bool:
        listt=list(s)
        ns,nt="",""
        l=len(listt)
        for i in range(l):
            if listt[l-i-1].isalnum():
                ns=ns+listt[l-i-1].lower()
            if listt[i].isalnum():
                nt=nt+listt[i].lower()
        print(ns)
        print(nt)
        if ns==nt:
            return True
        else:
            return False
                
                
            
        