class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, curr_min = 1, 1
        res = max(nums)
        
        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
                continue

            tmp = curr_max * n
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(tmp, curr_min * n, n)
            res = max(res, curr_max)

        return res