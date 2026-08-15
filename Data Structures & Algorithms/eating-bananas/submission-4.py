class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        min_hours = float("inf")
        while l <= r:
            m = l + (r - l) // 2

            total_hours = 0
            for b in piles:
                total_hours += (b + m - 1) // m
            
            if total_hours <= h:
                min_hours = min(min_hours, m)
                r = m - 1      
            else:
                l = m + 1

        return min_hours