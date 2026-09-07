class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_max = 0
        current_min = float("inf")

        for r in prices:
            current_min = min(current_min, r)
            max_profit = max(max_profit, r - current_min)

        return max_profit