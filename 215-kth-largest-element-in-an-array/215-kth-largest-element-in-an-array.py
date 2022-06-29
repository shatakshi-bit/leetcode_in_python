class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums=list(set(nums))
        heap=[]
        for i in nums:
            heappush(heap,i)
        for i in range(len(heap)-k):
            heappop(heap)
        return heappop(heap)
        
        # heap=[]
        # for i in nums:
        #     heappush(heap,i)
        # for i in range(k-1):
        #     heappop(heap)
        # return heappop(heap)
        