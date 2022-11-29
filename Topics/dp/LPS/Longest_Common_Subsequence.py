"""
https://leetcode.com/problems/longest-common-subsequence/
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        rows = len(text1) + 1
        cols = len(text2) + 1

        dp = [[0] * cols for _ in range(rows)]

        for row in range(1, rows):
            for col in range(1, cols):
                # same charecter on both string
                # add 1 and check left charecters which is matching
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    # not match
                    # check possibility by keeping one string constant and leaving a charecter
                    # which ever max out will be considered as a matching length
                    dp[row][col] = 0 + max(dp[row - 1][col], dp[row][col - 1])
        return dp[-1][-1]
