"""
https://leetcode.com/problems/minimum-falling-path-sum/description/

https://www.youtube.com/watch?v=N_aJ5qQbYA0
"""
import sys
from typing import List


class Solution:

    def dfs(self, matrix, row, col):
        """Not working, not able to root cause it"""
        if row < 0 or col < 0 or col >= len(matrix[0]):
            return sys.maxsize
        if row == 0:
            return matrix[row][col]

        up = matrix[row][col] + self.dfs(matrix, row-1, col)
        left_up = matrix[row][col] + self.dfs(matrix, row-1, col-1)
        right_up = matrix[row][col] + self.dfs(matrix, row-1, col+1)
        return min(left_up, up, right_up)
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # return self.dfs(matrix, len(matrix)-1, len(matrix[0])-1)
        grid = matrix.copy()
        n = len(matrix)
        for row in range(1, n):
            for col in range(n):
                if col == 0:
                    grid[row][col] += min(matrix[row - 1][col], matrix[row - 1][col + 1])
                elif col == n - 1:
                    grid[row][col] += min(matrix[row - 1][col], matrix[row - 1][col - 1])
                else:
                    grid[row][col] += min(matrix[row - 1][col], matrix[row - 1][col - 1], matrix[row - 1][col + 1])
        return min(grid[-1])



solve = Solution()
print(solve.minFallingPathSum(matrix=[[2,1,3],[6,5,4],[7,8,9]]))
