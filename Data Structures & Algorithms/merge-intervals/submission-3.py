class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]

        for start, finish in intervals[1:]:
            prev = merged[-1]

            if prev[1] >= start:
                if prev[1] > finish:
                    continue
                prev[1] = finish
            else:
                merged.append([start, finish])

        return merged
