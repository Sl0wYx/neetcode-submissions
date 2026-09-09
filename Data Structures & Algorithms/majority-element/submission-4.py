class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        count = 1
        candidate = nums[0]

        max_count = 0
        res = nums[0]
        for n in nums[1:]:
            if n != candidate:
                candidate = n
                count = 1

            if count > max_count:
                res = n
                max_count = count
            
            count += 1

        return res

        
