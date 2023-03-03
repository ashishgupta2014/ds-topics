"""
https://leetcode.com/problems/delete-operation-for-two-strings/description/

https://www.youtube.com/watch?v=yMnH0jrir0Q
"""
class Solution:

    def dfs(self, word1, word2, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        if i < 0 or j < 0:
            return 0

        if word1[i] == word2[j]:
            dp[(i, j)] = 1 + self.dfs(word1, word2, i-1, j-1, dp)
        else:
            dp[(i, j)] = max(self.dfs(word1, word2, i-1, j, dp), self.dfs(word1, word2, i, j-1, dp))
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
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = {}
        return n + m - 2* self.dfs(word1, word2, n-1, m-1, dp)

solve = Solution()
print(solve.minDistance(word1='sea', word2='eat'))
print(solve.minDistance(word1='leetcode', word2='etco'))