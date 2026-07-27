class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            need = target - numbers[r]
            if numbers[l] == need:
                return [l+1, r+1]
            elif numbers[l] < need:
                l += 1
            elif numbers[l] > need:
                r -= 1
            
            
        return []