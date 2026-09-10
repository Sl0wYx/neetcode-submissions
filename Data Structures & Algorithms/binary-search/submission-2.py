class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        for i in range(len(nums)):
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l += 1
            elif nums[m] > target:
                r -= 1

        return -1