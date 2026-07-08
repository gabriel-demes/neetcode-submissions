class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a min heap take the two biggest subtract them add back
        # to heap until heap is 1

        for i in range(len(stones)):
            stones[i] = -1 * stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                newStone = stone1 - stone2
            else:
                newStone = stone2 - stone1
            heapq.heappush(stones, -1 * newStone)
        
        if len(stones) == 1:
            return -1 * stones[0]
        else:
            return 0