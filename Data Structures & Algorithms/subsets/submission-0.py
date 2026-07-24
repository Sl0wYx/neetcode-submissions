class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        self.backtrack([], 0, nums)

        return self.result
    def backtrack(self, path, start, nums):
        self.result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(path, i+1, nums)
            path.pop()

            