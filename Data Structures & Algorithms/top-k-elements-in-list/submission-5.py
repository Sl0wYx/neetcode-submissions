class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        res = []

        for i in freq.keys():
            heapq.heappush(heap, (-freq[i], i))

        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
    
        return res