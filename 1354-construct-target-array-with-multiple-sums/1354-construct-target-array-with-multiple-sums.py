class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if (len(target)) == 1:
            if target == [1]:
                return True
            return False
        target.sort()
        if (sum(target) - target[-1]) > 0 and target[-1] / (sum(target) - target[-1]) > 1:
            target[-1] = target[-1]  - int(target[-1] / (sum(target) - target[-1]) - 1) * (sum(target) - target[-1])
        total = -sum(target)
        neg_target = []
        for num in target:
            neg_target.append(-num)
        heapq.heapify(neg_target)
        while heapq.nsmallest(1,neg_target)[0] < -1:
            min_val = heapq.heappop(neg_target)
            if (min_val - (total - min_val) >= 0):
                return False
            heapq.heappush(neg_target,min_val - (total - min_val))
            total = min_val
        if neg_target != [-1] * len(target):
            return False
        return True
            