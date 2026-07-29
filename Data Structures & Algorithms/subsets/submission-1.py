class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        self.backtrack([], 0, nums)

        return self.result
        
    def backtrack(self, path, start, nums):
        if start >= len(nums):
            self.result.append(path[:])
            return

        path.append(nums[start])
        self.backtrack(path, start+1, nums)
        path.pop()
        self.backtrack(path, start+1, nums)

            