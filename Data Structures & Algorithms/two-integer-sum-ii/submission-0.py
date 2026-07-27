class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            sum = target - numbers[i]
            if sum in seen and seen[sum]<i:
                return [seen[sum]+1, i+1]

            seen[numbers[i]] = i
            
        return []