"""
https://practice.geeksforgeeks.org/problems/rod-cutting0840/1

https://www.youtube.com/watch?v=mO8XpGoJwuo
"""
class Solution:

    def dfs(self, price, i, N, dp):
        if (i, N) in dp:
            return dp[(i, N)]
        if i == 0:
            return N*price[0]

        not_take = self.dfs(price, i-1, N, dp)
        take = 0
        rod_length = i+1
        if rod_length <= N:
            take = price[i] + self.dfs(price, i, N-rod_length, dp)
        dp[(i, N)] = max(not_take, take)
        return max(not_take, take)
    def tabular(self, price, n):
        dp = [[0]*(n+1) for _ in range(n)]

        for i in range(n+1):
            dp[0][i] = i*price[0]

        for i in range(1, n):
            for j in range(n+1):
                not_take = dp[i-1][j]
                rod_length = i+1
                take = 0
                if rod_length <= j:
                    take = price[i] + dp[i][j-rod_length]
                dp[i][j] = max(take, not_take)
        return dp[n-1][n]
    def cutRod(self, price, n):
        # dp = {}
        # return self.dfs(price, n-1, n, dp)
        return self.tabular(price, n)

solve = Solution()
print(solve.cutRod(price=[1, 5, 8, 9, 10, 17, 17, 20], n=8))