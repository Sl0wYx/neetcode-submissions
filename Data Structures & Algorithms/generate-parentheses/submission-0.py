class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenth = []
        self.stack = []
        self.res = []

        self.backtrack(0, 0, n)

        return self.res


    def backtrack(self, open, closed, n):
        if closed == open == n:
            self.res.append("".join(self.stack))
            return
    
        if open < n:
            self.stack.append('(')
            self.backtrack(open+1, closed, n)
            self.stack.pop()
        
        if closed < open:
            self.stack.append(')')
            self.backtrack(open, closed + 1, n)
            self.stack.pop()

