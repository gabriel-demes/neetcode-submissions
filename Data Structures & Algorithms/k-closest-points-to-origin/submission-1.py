class Solution:
    def distance(self, arr):
        d = arr[0] ** 2 + arr[1] ** 2
        return d

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        distancesHeap = []

        for i in points:
            d = self.distance(i)
            distances.append([d, i[0], i[1]])

        heapq.heapify(distances)

        res = []
        while k > 0:
            distance = heapq.heappop(distances)
            res.append([distance[1], distance[2]])
            k -= 1
        
        return res
        