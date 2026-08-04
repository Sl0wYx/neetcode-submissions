import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = []

        for w in stones:
            heapq.heappush(weights, -w)

        while len(weights) > 1:
            x = -heapq.heappop(weights)
            y = -heapq.heappop(weights)
            if x < y:
                heapq.heappush(weights, -(y - x))
            elif x > y:
                heapq.heappush(weights, -(x - y))
            elif x == y:
                continue

        return -weights[0] if weights else 0
