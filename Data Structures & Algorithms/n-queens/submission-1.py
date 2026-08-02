class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.col = set()
        self.pos_diag = set()
        self.neg_diag =  set()

        self.board = [["."] * n for i in range(n)]
        self.res = []

        self.backtrack(0, n)

        return self.res

    def backtrack(self, r, n):
        if r == n:
            copy = [''.join(row) for row in self.board]
            self.res.append(copy)
            return
        
        for c in range(n):
            if c in self.col or (r+c) in self.pos_diag or r-c in self.neg_diag:
                continue

            self.col.add(c)
            self.pos_diag.add(r+c)
            self.neg_diag.add(r-c)
            self.board[r][c] = 'Q'

            self.backtrack(r + 1, n)

            self.col.remove(c)
            self.pos_diag.remove(r+c)
            self.neg_diag.remove(r-c)
            self.board[r][c] = '.'