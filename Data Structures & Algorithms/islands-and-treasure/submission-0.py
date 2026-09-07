class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        distance = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = distance + 1
                        queue.append((nr,nc))

            distance += 1

