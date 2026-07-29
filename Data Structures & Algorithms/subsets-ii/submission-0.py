class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.backtrack([], nums, 0)

        return self.res

    def backtrack(self, path, nums, i):
        if i >= len(nums):
            self.res.append(path[:])
            return

        path.append(nums[i])
        self.backtrack(path, nums, i+1)
        path.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

        self.backtrack(path, nums, i+1)