class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = Counter(arr)

        distinct = []
        for c in arr:
            if seen[c] < 2:
                distinct.append(c)

            if len(distinct) == k:
                return c

        return ""