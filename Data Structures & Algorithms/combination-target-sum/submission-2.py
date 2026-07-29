class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []

        self.backtracking([], 0, nums, target, 0)
        
        return self.result
    
    def backtracking(self, path, i, nums, target, total):
        if total == target:
            self.result.append(path[:])
            return

        if total > target or i >= len(nums):
            return
        
        path.append(nums[i])
        self.backtracking(path, i, nums, target, total+nums[i])
        path.pop()
        self.backtracking(path, i+1, nums, target, total)