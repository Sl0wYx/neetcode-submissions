class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()
        self.backtrack([], 0, 0, candidates, target)

        return self.res

    def backtrack(self, path, i, total, nums, target):
        if total == target:
            self.res.append(path[:])
            return
        if total > target or i == len(nums):
            return
        
        path.append(nums[i])
        self.backtrack(path, i+1, total + nums[i], nums, target)
        path.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

        self.backtrack(path, i+1, total, nums, target)