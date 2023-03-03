"""
https://leetcode.com/problems/unique-paths-ii/description/

https://www.youtube.com/watch?v=TmhpgXScLyY
"""
from typing import List


class Solution:

    def dfs(self, matrix, row, col):
        if row == 0 and col == 0:
            return 1
        if row < 0 or col < 0 or matrix[row][col]:
            return 0
        left = self.dfs(matrix, row, col-1)
        up = self.dfs(matrix, row-1, col)
        return left+up

    def tabular(self, matrix):
        if matrix[0][0] == 1:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        dp[0][1] = 1
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if not matrix[row-1][col-1]:
                    dp[row][col] = dp[row][col-1] + dp[row-1][col]
        return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # rows = len(obstacleGrid)-1
        # cols = len(obstacleGrid[0])-1
        # return self.dfs(obstacleGrid, rows, cols)
        return self.tabular(obstacleGrid)

solve = Solution()
print(solve.uniquePathsWithObstacles(obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]))
print(solve.uniquePathsWithObstacles(obstacleGrid=[[0,1],[0,0]]))
print(solve.uniquePathsWithObstacles(obstacleGrid=[[1,0]]))
print(solve.uniquePathsWithObstacles(obstacleGrid=[[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))