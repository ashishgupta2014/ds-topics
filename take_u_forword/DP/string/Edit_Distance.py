"""
https://leetcode.com/problems/edit-distance/

https://www.youtube.com/watch?v=fJaKO8FbDdo
"""
class Solution:

    def dfs(self, word1, word2, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        if i < 0:
            return j+1
        if j < 0:
            return i+1

        if word1[i] == word2[j]:
            dp[(i, j)] = self.dfs(word1, word2, i-1, j-1, dp)
        else:
            dp[(i, j)] = 1 + min(self.dfs(word1, word2, i-1, j, dp),
                           self.dfs(word1, word2, i, j-1, dp),
                           self.dfs(word1, word2, i-1, j-1, dp))
        return dp[(i, j)]

    def tabular(self, word1, word2):
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j

        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    def minDistance(self, word1: str, word2: str) -> int:

        # return self.dfs(word1, word2, len(word1)-1, len(word2)-1, {})
        return self.tabular(word1, word2)

solve = Solution()
print(solve.minDistance(word1='horse', word2='ros'))
