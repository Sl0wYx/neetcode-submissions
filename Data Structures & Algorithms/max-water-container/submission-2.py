class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        max_size = 0

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            max_size = max(max_size, area)

            if heights[r] > heights[l]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                r -= 1
                l += 1

        return max_size