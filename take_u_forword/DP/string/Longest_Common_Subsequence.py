"""
https://leetcode.com/problems/longest-common-subsequence/description/

https://www.youtube.com/watch?v=NPZn9jBrX8U
"""
class Solution:

    def dfs(self, text1, text2, i, j, dp):
        if i < 0 or j < 0:
            return 0
        if (i, j) in dp:
            return dp[(i, j)]

        if text1[i] == text2[j]:
            dp[(i, j)] = 1 + self.dfs(text1, text2, i-1, j-1, dp)
            return dp[(i, j)]

        dp[(i, j)] = max(self.dfs(text1, text2, i-1, j, dp), self.dfs(text1, text2, i, j-1, dp))
        return dp[(i, j)]

    def tabular(self, text1, text2):
        n = len(text1)
        m = len(text2)

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp = {}
        # return self.dfs(text1, text2, len(text1)-1, len(text2)-1, dp)
        return self.tabular(text1, text2)

solve = Solution()
print(solve.longestCommonSubsequence(text1='abcde', text2='ace'))
print(solve.longestCommonSubsequence(text1='abc', text2='abc'))
print(solve.longestCommonSubsequence(text1='abc', text2='def'))
print(solve.longestCommonSubsequence(text1='abaaa', text2='baabaca'))