import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        
        self.heap_nums = []
        for n in self.nums:
            heapq.heappush(self.heap_nums, n)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap_nums, val)
        while len(self.heap_nums) > self.k:
            heapq.heappop(self.heap_nums)

        res = heapq.heappop(self.heap_nums)
        heapq.heappush(self.heap_nums, res)
        return res
        

        