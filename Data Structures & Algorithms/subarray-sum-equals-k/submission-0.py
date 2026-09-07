class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        current_sum = 0
        answer = 0

        for n in nums:
            current_sum += n
            answer += count.get(current_sum - k, 0)
            count[current_sum] = count.get(current_sum, 0) + 1

        return answer

