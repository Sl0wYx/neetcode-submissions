class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        whole_sum = sum(nums)

        left_sum = 0
        for i in range(len(nums)):
            left_sum += nums[i]
            if left_sum == whole_sum:
                return i
            whole_sum -= nums[i]

        return -1
