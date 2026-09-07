class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        grid = {i:[] for i in range(numCourses)}
    
        for i, course in prerequisites:
            grid[i].append(course)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if grid[crs] == []:
                return True

            visited.add(crs)
            for pre in grid[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            grid[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True