class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return sorted(list(set(nums))) != sorted(nums)