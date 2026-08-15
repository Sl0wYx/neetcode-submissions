class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        min_value = float("inf")
        while l <= r:
            m = l + (r - l) // 2

            min_value = min(min_value, nums[m])
            if nums[m] >= nums[r]:
                l += 1
            elif nums[m] <= nums[r]:
                r -= 1

        return min_value
            