class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        grid = {x:[] for x in range(n)}

        for node, edge in edges:
            grid[node].append(edge)
            grid[edge].append(node)

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for edge in grid[node]:
                dfs(edge)


        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count
                
                    