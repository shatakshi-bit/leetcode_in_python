class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeros_ones = []
        for s in strs:
            zero_cnt = 0
            one_cnt = 0
            for c in s:
                if c == '0':
                    zero_cnt += 1
                elif c == '1':
                    one_cnt += 1
            zeros_ones.append((zero_cnt, one_cnt))
        zeros_ones.sort()
        
        dp_ones = [(-1, 0)] * (n + 1)
        dp_ones[0] = (0,0)
        for z, o in zeros_ones:
            for i in reversed(range(n + 1 - o)):
                if dp_ones[i][0] >= 0 and \
                    dp_ones[i][1] + z <= m and \
                    dp_ones[i + o][0] < dp_ones[i][0] + 1:
                        dp_ones[i + o] = (dp_ones[i][0] + 1, dp_ones[i][1] + z)
        return max((t[0] for t in dp_ones))