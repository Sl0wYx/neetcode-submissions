class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.result = []

        self.backtracking([], 0, nums, target)
        
        return self.result
    
    def backtracking(self, path, start, nums, target):
        path_sum = 0
        for n in path:
            path_sum += n
            if path_sum > target:
                return

        if path_sum == target:
            self.result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtracking(path, i, nums, target)
            path.pop()