class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dup = set(nums)
        return sorted(list(no_dup)) != sorted(nums)
        