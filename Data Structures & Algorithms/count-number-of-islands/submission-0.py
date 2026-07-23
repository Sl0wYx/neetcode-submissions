from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #print(grid[i][j])
                if grid[i][j] == "1":
                    self.count += 1
                    self.bfs(grid, i, j)
    
        return self.count

    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < len(grid) and nc < len(grid[0]) and nr >= 0 and nc >= 0 and grid[nr][nc] != "0":
                    print(nr,nc)
                    queue.append((nr,nc))
                    grid[nr][nc] = "0"


