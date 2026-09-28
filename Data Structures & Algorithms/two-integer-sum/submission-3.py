class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen hash: number -> index
        # for loop through every number
        # if compliment (target - current number) is in the seen, return compliment index and current number index
        # else add current number -> current index to the seen hash

        seen = {} # number -> index

        for i, n in enumerate(nums):
            compliment = target - n

            if compliment in seen:
                return [seen[compliment], i]

            seen[n] = i