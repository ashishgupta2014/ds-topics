"""
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

https://www.youtube.com/watch?v=GqOmJHQZivw
"""
class Solution:

    def dfs(self, W, wt, val, n, dp):
        if (W, n) in dp:
            return dp[W, n]
        if n < 0:
            return 0
        not_take = 0 + self.dfs(W, wt, val, n-1, dp)
        take = 0
        if wt[n] <= W:
            take = val[n] + self.dfs(W-wt[n], wt, val, n-1, dp)
        dp[(W, n)] = max(not_take, take)
        return max(not_take, take)

    def tabular(self, W, wt, val, n):
        dp = [[0]*(W+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, W+1):
                not_take = dp[i-1][j]
                take = 0
                if wt[i-1] <= j:
                    take = val[i-1] + dp[i-1][j-wt[i-1]]
                dp[i][j] = max(not_take, take)
        return dp[-1][-1]
    def knapSack(self, W, wt, val, n):
        # dp = {}
        # return self.dfs(W, wt, val, n-1, dp)
        return self.tabular(W, wt, val, n)

solve = Solution()
print(solve.knapSack(W=4, wt=[4,5,1], val=[1,2,3], n=3))
print(solve.knapSack(W=8, wt=[3, 4, 5], val=[30, 50, 60], n=3))