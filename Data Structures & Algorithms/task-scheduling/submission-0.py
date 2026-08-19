class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-val_count for val_count in count.values()]
        heapq.heapify(max_heap)

        time = 0 
        queue = deque()

        while max_heap or queue:
            time += 1

            if max_heap:
                val_count = 1 + heapq.heappop(max_heap)
                if val_count:
                    queue.append([val_count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time
