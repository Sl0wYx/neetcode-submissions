class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        seen = set()
        grid = {x:[] for x in range(n)}

        for edge, node in edges:
            grid[edge].append(node)
            grid[node].append(edge)

        visited = set()
        def dfs(edge, parent):
            if edge in visited:
                return False

            visited.add(edge)

            for node in grid[edge]:
                if node == parent:
                    continue

                if not dfs(node, edge):
                    return False

            return True
        
        if not dfs(0, -1):
            return False

        if len(visited) != n:
            return False

        return True

            
