class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        grid = {x+1:[] for x in range(len(edges))}
        
        def dfs(node, target, visited):
            if node == target:
                return True

            visited.add(node)
            
            for edge in grid[node]:
                if edge not in visited:
                    if dfs(edge, target, visited):
                        return True
            
            return False

        for node, edge in edges:
            if dfs(node, edge, set()):
                return [node, edge]
            grid[node].append(edge)
            grid[edge].append(node)

        return edge[-1]