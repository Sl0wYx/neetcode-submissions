class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        res = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r, c, ocean):
            if ocean == "pac":
                pac.add((r,c))
                check = pac
            elif ocean == "atl":
                atl.add((r,c))
                check = atl

            if (r, c) in pac and (r, c) in atl:
                res.add((r,c))
            

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < len(heights) and 0 <= nc < len(heights[nr]) 
                and heights[nr][nc] >= heights[r][c]
                and (nr, nc) not in check):
                    dfs(nr, nc, ocean)

        
        for r in range(len(heights)):
            dfs(r, 0, "pac")
            dfs(r, len(heights[r]) - 1, "atl")

        for c in range(len(heights[0])):
            dfs(0, c, "pac")
            dfs(len(heights) - 1, c, "atl")
        
        return list(res)