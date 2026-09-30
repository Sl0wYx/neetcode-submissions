class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create result list
        # imagine ones on both ends \
        # multiply each value to the previous one (left to the right)
        # multipying each value to previous one again (right to the left)
        # return result list

        result = [1] * len(nums)

        prev = 1
        for i in range(len(nums)):
            result[i] = prev
            prev *= nums[i]
        
        prev = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] *= prev
            prev *= nums[j]

        return result

        
