"""
https://leetcode.com/problems/distinct-subsequences/description/

https://www.youtube.com/watch?v=nVG7eTiD2bY
"""
class Solution:

    def dfs(self, s, t, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        if j < 0:
            return 1
        if i < 0:
            return 0
        if s[i] == t[j]:
            dp[(i, j)] = self.dfs(s, t, i-1, j-1, dp) + self.dfs(s, t, i-1, j, dp)
        else:
            dp[(i, j)] = self.dfs(s, t, i-1, j, dp)
        return dp[(i, j)]

    def tabular(self, s, t):
        n = len(s)
        m = len(t)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][m]


    def numDistinct(self, s: str, t: str) -> int:
        # dp = {}
        # return self.dfs(s, t, len(s)-1, len(t)-1, dp)
        return self.tabular(s, t)

solve = Solution()
print(solve.numDistinct(s='rabbbit', t='rabbit'))
print(solve.numDistinct(s='babgbag', t='bag'))