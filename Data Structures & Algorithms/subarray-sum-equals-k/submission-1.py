class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0:1}
        current_prefix = 0
        answer = 0

        for n in nums:
            current_prefix += n
            answer += count.get(current_prefix - k, 0)
            count[current_prefix] = count.get(current_prefix, 0) + 1

        return answer