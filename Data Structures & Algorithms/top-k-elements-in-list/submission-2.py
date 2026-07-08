class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, total in count.items():
            freq[total].append(num)
        
        topFreq = []
        for arr in range(len(freq) -1, 0, -1):
            topFreq.extend(freq[arr])
            if len(topFreq) == k:
                return topFreq