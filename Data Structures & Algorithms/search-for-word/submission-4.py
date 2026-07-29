class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0]:
                    if self.dfs(board, word, r, c, 1):
                        return True

        return False
    def dfs(self, grid, word, r, c, i):
        if i == len(word):
            return True
        if not grid:
            return False
        if i >= len(word):
            return False
        original = grid[r][c]
        grid[r][c] = '#'
        demensions = [(1,0), (0, 1), (-1, 0), (0,-1)]
        for dr, dc in demensions:
            nr, nc = r + dr, c + dc

            if nr < len(grid) and nc < len(grid[0]) and nr >= 0 and nc >= 0 and grid[nr][nc] == word[i]:
                if self.dfs(grid, word, nr,nc,i+1):
                    grid[nr][nc] = original
                    return True
        grid[r][c] = original
        return False
