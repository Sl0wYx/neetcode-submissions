class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for start, end in intervals:
            prev = merged[-1]

            if prev[1] >= start:
                prev[1] = max(prev[1], end)
            else:
                merged.append([start, end])

        return merged