import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        self.nums_heap = []
        for n in self.nums:
            heapq.heappush(self.nums_heap, n)

    def add(self, val: int) -> int:
        if self.nums == None:
            return None

        heapq.heappush(self.nums_heap, val)
        temp_heap = self.nums_heap.copy()
        heap_length = len(temp_heap)
        i = 0 
        while i < heap_length-self.k:
            heapq.heappop(temp_heap)
            i += 1
        
        return heapq.heappop(temp_heap)
        