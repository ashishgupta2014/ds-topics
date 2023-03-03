"""
https://leetcode.com/problems/triangle/description/

https://www.youtube.com/watch?v=SrP-PiLSYC0
"""
import sys
from typing import List


class Solution:

    def dfs(self, triangle, i, j, dp):
        if i >= len(triangle) or j >= len(triangle[-1]):
            return sys.maxsize
        if dp[i][j] != -1:
            return dp[i][j]
        if i == len(triangle)-1:
            return triangle[i][j]
        down = triangle[i][j] + self.dfs(triangle, i+1, j, dp)
        diagonal = triangle[i][j] + self.dfs(triangle, i+1, j+1, dp)
        dp[i][j] = min(down, diagonal)
        return min(down, diagonal)

    def tabular(self, triangle):
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                down = triangle[i][j] + dp[i+1][j]
                diagonal = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down, diagonal)
        return dp[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp = [[-1]*len(triangle) for _ in range(len(triangle))]
        # return self.dfs(triangle, 0, 0, dp)
        return self.tabular(triangle)

solve = Solution()
print(solve.minimumTotal(triangle=[[2],[3,4],[6,5,7],[4,1,8,3]]))
print(solve.minimumTotal(triangle=[[-10]]))
print(solve.minimumTotal(triangle=[[-1],[2,3],[1,-1,-3]]))
