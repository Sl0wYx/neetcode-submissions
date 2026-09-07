class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        dimensions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        time = 0

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                print(r,c)
                for dr, dc in dimensions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
                    
            time += 1

        return time if fresh == 0 else -1