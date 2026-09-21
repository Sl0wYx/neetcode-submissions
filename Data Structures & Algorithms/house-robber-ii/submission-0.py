class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_houses(houses):
            rob1, rob2 = 0, 0
            for n in houses:
                current = max(rob1, rob2 + n)
                rob2 = rob1
                rob1 = current

            return rob1

        return max(rob_houses(nums[1:]), rob_houses(nums[:-1]))

        