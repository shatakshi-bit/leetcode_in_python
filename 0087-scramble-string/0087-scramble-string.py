class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # Initialize a 3D table to store the results of all possible substrings of the two strings
        dp = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n+1)]

        # Initialize the table for substrings of length 1
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        # Fill the table for substrings of length 2 to n
        for length in range(2, n+1):
            for i in range(n+1-length):
                for j in range(n+1-length):
                    # Iterate over all possible lengths of the first substring
                    for newLength in range(1, length):
                        # Check if the two possible splits of the substrings are scrambled versions of each other
                        dp1 = dp[newLength][i]
                        dp2 = dp[length-newLength][i+newLength]
                        dp[length][i][j] |= dp1[j] and dp2[j+newLength]
                        dp[length][i][j] |= dp1[j+length-newLength] and dp2[j]

        # Return whether the entire strings s1 and s2 are scrambled versions of each other
        return dp[n][0][0]
        