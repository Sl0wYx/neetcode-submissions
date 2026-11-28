from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def f(i):
            if i == n:
                return 1
            
            if i > n:
                return 0
            
            return f(i + 1) + f(i + 2)

        return f(0)