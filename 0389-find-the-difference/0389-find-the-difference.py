# Time complexity: O(n)
# Space: O(1)
# From XOR characteristics
# 0 ^ x = x
# x ^ x = 0, x is any number
# So, if we use 0 to XOR both str s and t. The last value will be ASCII of difference character

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for i in range(len(s)):
            ans = ans ^ ord(s[i]) ^ ord(t[i])
        ans ^= ord(t[-1])
        return chr(ans)
        