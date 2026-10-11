class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float("inf")
        max_proffit = 0

        for n in prices:
            if n < buy:
                buy = n

            max_proffit = max(max_proffit, n - buy)

        return max_proffit
        