class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] == nums[r] or nums[r] in seen or nums[l] in seen:
                return True
            
            seen.add(nums[l])
            seen.add(nums[r])
            l += 1
            r -= 1

        return False