"""
https://leetcode.com/problems/edit-distance/
https://www.youtube.com/watch?v=XYi2-LPrwm4
"""


class Solution:
    def minDistance(self, source: str, target: str) -> int:
        rows = len(source) + 1
        cols = len(target) + 1
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if row == 0:
                    dp[row][col] = col
                elif col == 0:
                    dp[row][col] = row
                elif source[row - 1] == target[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    dp[row][col] = 1 + min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1])
        return dp[rows - 1][cols - 1]


solve = Solution()
word1 = "horse"
word2 = "ros"
print(solve.minDistance(word1, word2))
