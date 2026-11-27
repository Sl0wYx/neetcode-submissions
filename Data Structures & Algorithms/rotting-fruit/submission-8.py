class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        
            if queue:
                count += 1

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1
        
        return count