class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for p in points:
            x = p[0]
            y = p[1]
            distance = ((x - 0)**2 + (y - 0)**2) ** (1/2)

            if len(min_heap) >= k:
                if -min_heap[0][0] < distance:
                    continue
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, (-distance, p))
        
        print(min_heap)
        res = []
        for p in min_heap:
            res.append(p[1])

        return res