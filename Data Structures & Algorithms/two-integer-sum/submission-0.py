class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            sum = target - nums[i]

            if sum in seen:
                return [seen[sum], i]

            seen[nums[i]] = i

        return []