class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create count dict which counts nums frequencies
        # empty heap - min_heap with numbers
        # for loop in count.items()
        # heappush the tuple (freq, number) to the min_heap
        # if length of heap is greater than k heappop from the heap
        # result list
        # while loop - heappop number (wich is [1]) to the result list
        # return result

        counts = Counter(nums)
        min_heap = []

        for number, count in counts.items():
            heapq.heappush(min_heap, (count, number))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])

        return result
