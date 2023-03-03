"""
https://leetcode.com/problems/unique-paths/description/

https://www.youtube.com/watch?v=sdE0A2Oxofw
"""
class Solution:

    def dfs(self, rows, cols, row, col):
        if row == rows-1 and col == cols-1:
            return 1
        if row >= rows or col >= cols:
            return 0
        right = self.dfs(rows, cols, row, col+1)
        down = self.dfs(rows, cols, row+1, col)
        return right + down

    def tabular(self, rows, cols):
        dp = [[0]*cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row][col-1] + dp[row-1][col]
        return dp[-1][-1]
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.dfs(m, n, 0, 0)
        return self.tabular(m, n)

solve = Solution()
print(solve.uniquePaths(m=3, n=7))
print(solve.uniquePaths(m=3, n=2))
