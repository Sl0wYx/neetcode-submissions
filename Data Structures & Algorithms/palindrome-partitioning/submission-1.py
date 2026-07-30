class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs([], s, 0)
        return self.res
    def dfs(self, path, s, i):
        if i >= len(s):
            self.res.append(path[:])
            return

        for j in range(i, len(s)):
            if self.isPalin(s, i, j):
                path.append(s[i:j+1])
                self.dfs(path, s, j+1)
                path.pop()
    def isPalin(self, s, i, j):
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True
    
