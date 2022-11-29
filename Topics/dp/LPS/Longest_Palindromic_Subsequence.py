"""
https://leetcode.com/problems/longest-palindromic-subsequence/
https://www.youtube.com/watch?v=NPZn9jBrX8U
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        x = s[::-1]

        rows = cols = len(s) + 1

        dp = [[0] * cols for _ in range(rows)]

        for row in range(1, rows):
            for col in range(1, cols):
                # same charecter on both string
                # add 1 and check left charecters which is matching
                if s[row - 1] == x[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    # not match
                    # check possibility by keeping one string constant and leaving a charecter
                    # which ever max out will be considered as a matching length
                    dp[row][col] = 0 + max(dp[row - 1][col], dp[row][col - 1])
        return dp[-1][-1]
