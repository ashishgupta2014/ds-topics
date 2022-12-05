"""
https://workat.tech/problem-solving/practice/median-row-sorted-matrix
https://www.youtube.com/watch?v=63fPPOdIr2c
"""


from bisect import bisect_right as upper_bound


class Solution:
    def calculateMedianOfMatrix(self, matrix) -> int:
        low = float('inf')
        high = float('-inf')
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][cols - 1])

        requiredIndx = (rows * cols + 1) // 2

        while low < high:
            mid = low + (high - low) // 2
            index = 0

            for i in range(rows):
                index += upper_bound(matrix[i], mid)
            if index < requiredIndx:
                low = mid + 1
            else:
                high = mid
        return low


solve = Solution()

mat = [[1, 2, 3],
[3, 3, 4],
[1, 1, 2]]

print(solve.calculateMedianOfMatrix(mat))


