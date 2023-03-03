"""
https://leetcode.com/problems/minimum-path-sum/description/

https://www.youtube.com/watch?v=_rgTlyky1uQ
"""
import sys
from typing import List


class Solution:

    def dfs(self, grid, row, col):
        if row == 0 and col == 0:
            return grid[0][0]
        if row < 0 or col < 0:
            return sys.maxsize
        up = grid[row][col] + self.dfs(grid, row-1, col)
        left = grid[row][col] + self.dfs(grid, row, col - 1)
        return min(left, up)

    def tabular(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col > 0:
                    grid[row][col] += grid[row][col-1]
                elif col == 0 and row > 0:
                    grid[row][col] += grid[row-1][col]
                elif row > 0 and col > 0:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        return grid[-1][-1]
    def minPathSum(self, grid: List[List[int]]) -> int:
        # rows = len(grid)-1
        # cols = len(grid[0])-1
        # return self.dfs(grid, rows, cols)
        return self.tabular(grid)


solve = Solution()
print(solve.minPathSum(grid=[[1,3,1],
                             [1,5,1],
                             [4,2,1]]))
