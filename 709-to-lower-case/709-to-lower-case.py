class Solution:
    def toLowerCase(self, s: str) -> str:
        # print(ord('a'),ord('z'))
        # print(ord('A'),ord('Z'))
        s1=''
        for i in s:
            if ord(i)>=65 and ord(i)<=90:
                s1=s1+chr(ord(i)+32)
            else:
                s1=s1+i
        return s1