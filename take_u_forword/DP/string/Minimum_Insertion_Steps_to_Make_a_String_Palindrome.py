"""
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

https://www.youtube.com/watch?v=xPBLEj41rFU
"""
class Solution:

    def dfs(self, s1, s2, i, j, dp):
        if i < 0 or j < 0:
            return 0
        if (i, j) in dp:
            return dp[(i, j)]
        if s1[i] == s2[j]:
            dp[(i, j)] = 1 + self.dfs(s1, s2, i-1, j-1, dp)
            return dp[(i, j)]
        else:
            dp[(i, j)] = max(self.dfs(s1, s2, i-1, j, dp), self.dfs(s1, s2, i, j-1, dp))
            return dp[(i, j)]

    def tabular(self, s1, s2):
        n = len(s1)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    def minInsertions(self, s: str) -> int:
        n = len(s)
        # lcs = self.dfs(s, s[::-1], n-1, n-1, {})
        lcs = self.tabular(s, s[::-1])
        return n - lcs
solve = Solution()
print(solve.minInsertions(s='leetcode'))