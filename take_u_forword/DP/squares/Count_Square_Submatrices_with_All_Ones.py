"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

https://www.youtube.com/watch?v=auS1fynpnjo
"""
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*cols for _ in range(rows)]

        for row in range(rows):
            dp[row][0] = matrix[row][0]
        for col in range(cols):
            dp[0][col] = matrix[0][col]

        max_square = sum(dp[0])
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col]:
                    dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1]) + 1
            max_square += sum(dp[row])
        return max_square



solve = Solution()
print(solve.countSquares(matrix=[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))