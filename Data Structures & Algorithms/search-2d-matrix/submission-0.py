class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            l, r = 0, len(row) - 1
            while l <= r:
                m = r - l + 1 // 2

                if row[m] == target:
                    return True
                elif row[m] < target:
                    l += 1
                elif row[m] > target:
                    r -= 1

        return False
                