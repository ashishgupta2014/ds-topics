"""
https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1

https://www.youtube.com/watch?v=_wP9mWNPL5w
"""
class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        n = len(S1)
        m = len(S2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        max_lcs = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if S1[i - 1] == S2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    max_lcs = max(max_lcs, dp[i][j])
        return max_lcs


solve = Solution()
print(solve.longestCommonSubstr(S1='ABCDGH', S2='ACDGHR', n=6, m=6))