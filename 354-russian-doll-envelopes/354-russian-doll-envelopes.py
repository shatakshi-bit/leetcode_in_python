class Solution:
    def maxEnvelopes(self, E: List[List[int]]) -> int:
        E.sort(key=lambda x: (x[0], -x[1]))
        res_h = [E[0][1]]
        for i in range(1, len(E)):
            w, h = E[i]
            if w == E[i-1]:
                continue
            # find the smallest index that's larger than h
            # if it doesn't exist, append the new h in the end; otherwise replace the current smallest with the new h
            left = bisect_left(res_h, h)
            if left == len(res_h): res_h.append(h)
            else: res_h[left] = h
        return len(res_h)
        