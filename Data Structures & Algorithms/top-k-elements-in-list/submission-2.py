from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        sorted_freq = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        return sorted_freq[:k]
