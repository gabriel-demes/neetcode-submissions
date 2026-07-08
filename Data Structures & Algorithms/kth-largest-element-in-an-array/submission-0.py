class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heap.append(-i)
        
        heapq.heapify(heap)

        num = 0
        while k > 0:
            num = heapq.heappop(heap)
            k -= 1
        return 0 - num