class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        grid = {x:[] for x in range(numCourses)}

        for c, p in prerequisites:
            grid[c].append(p)

        def dfs(crs, visited):
            if crs in visited:
                return False
            
            if not grid[crs]:
                return True

            visited.add(crs)

            for p in grid[crs]:
                if not dfs(p, visited):
                    return False

            visited.remove(crs)
            grid[crs] = []
            return True
        
        for p in range(numCourses):
            if not dfs(p, set()):
                return False

        return True