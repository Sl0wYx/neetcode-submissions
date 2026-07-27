class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1]:
                continue

            i, k = j + 1, len(nums)-1
            while i < k:
                res = nums[j] + nums[i] + nums[k]
                if res == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    i += 1
                    k -= 1
                    
                    while i < k and nums[i] == nums[i-1]:
                        i += 1
                    
                    while i < k and nums[k] == nums[k+1]:
                        k -= 1
                elif res < 0:
                    i += 1
                elif res > 0:
                    k -= 1
        
        return ans