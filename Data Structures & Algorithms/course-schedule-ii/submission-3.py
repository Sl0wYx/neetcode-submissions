class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        
        grid = {x:[] for x in range(numCourses)}

        for course, required in prerequisites:
            grid[course].append(required)
        
        visited = set()
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True

            visiting.add(course)

            for pre in grid[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            if course not in res:
                res.append(course)

            return True

        for i in range(numCourses):
            check = dfs(i)
            if not check:
                return []

        return res