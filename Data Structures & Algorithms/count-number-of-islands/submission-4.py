class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(r, c):
            grid[r][c] = "0"
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[nr]) and grid[nr][nc] == "1":
                    dfs(nr, nc)

        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count