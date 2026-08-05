class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        max_size = 0

        while l < r:
            max_size = max(max_size, max(r - l, 1) * min(heights[r], heights[l]))

            if heights[r] > heights[l]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                r -= 1
                l += 1

        return max_size