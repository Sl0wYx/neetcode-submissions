class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(r, c):
            count = 1
            grid[r][c] = "X"
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]) and grid[nr][nc] == 1:
                    count += dfs(nr, nc)
            return count

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    count = dfs(r, c)
                    max_area = max(max_area, count)

        return max_area
