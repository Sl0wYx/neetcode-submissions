class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        self.mapping = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        self.backtracking([], 0, digits)

        return self.res
    
    def backtracking(self, path, i, digits):
        if i >= len(digits):
            if path:
                self.res.append(''.join(path[:]))
            return
        if len(path) >= len(digits):
            return

        
        for c in self.mapping[digits[i]]:
            path.append(c)
            self.backtracking(path, i+1, digits)
            path.pop()

                                