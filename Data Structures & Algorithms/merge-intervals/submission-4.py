class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for start, finish in intervals:
            prev = merged[-1]

            if prev[1] >= start:
                if prev[1] < finish:
                    merged[-1] = [prev[0], finish]
            else:
                merged.append([start, finish])

        return merged