class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1, 1, 1, 1, 1]  ## initial 
        for i in range(2, n+1):   ## for different values of n
            for j in range(5):   ## for 5 vowels
                arr[j] = sum(arr[j:])
        return sum(arr)  