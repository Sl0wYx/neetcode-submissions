class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        expected = 0

        for got in nums:
            if expected != got:
                return expected
            
            expected += 1

        return expected