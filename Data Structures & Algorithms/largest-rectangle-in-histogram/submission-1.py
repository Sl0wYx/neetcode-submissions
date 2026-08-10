class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        res = 0
        for i in range(len(heights)):
            new_i = i
            while stack and stack[-1][1] >= heights[i]:
                new_i, h = stack.pop()
                res = max(res, h * (i - new_i))
            
            stack.append((new_i, heights[i]))

        for i, h in stack:
            rectangle = h * (len(heights) - i)
            res = max(res, rectangle)
        
        return res