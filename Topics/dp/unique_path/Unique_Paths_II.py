"""
https://leetcode.com/problems/unique-paths-ii/
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if not obstacleGrid[row - 1][col - 1]:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]


solve = Solution()
# matrix = [[0, 1], [0, 0]]
# matrix = [[1, 0]]
matrix = [[0, 0], [1, 1], [0, 0]]
# matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(solve.uniquePathsWithObstacles(matrix))
