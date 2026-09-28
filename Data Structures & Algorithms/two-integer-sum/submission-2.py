class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Only one possible answer
        # Return indices of numbers that sum to target
        # What to look for: nums[j] = target - nums[i]

        # Create seen hashmap with value-to-indice map
        # As we iterate through the nums, we check if target - current number is in the hashmap
        # In the same loop add the current number to the hashmap (mark it as seen)
        # If target - current number is in the seen hash, we return indices of both found value and the current number

        # Edge cases:
        # Single value - not possible (nums length > 2)
        # All zero always false, one zero doesnt impact anything
        # Negative values - works without changes

        seen = {} # number:j

        for i in range(len(nums)):
            find = target - nums[i]

            if find in seen:
                return [seen[find], i]

            seen[nums[i]] = i
