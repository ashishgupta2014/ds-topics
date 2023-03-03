"""
https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1

https://www.youtube.com/watch?v=OgvOZ6OrJoY
"""
class Solution:

    def dfs(self, N, W, val, wt, dp):

        if (N, W) in dp:
            return dp[(N, W)]
        if N == 0:
            return W//wt[0] * val[0]

        not_take = 0 + self.dfs(N-1, W, val, wt, dp)
        take = float('-inf')
        if wt[N] <= W:
            take = val[N] + self.dfs(N, W-wt[N], val, wt, dp)
        dp[(N, W)] = max(not_take, take)
        return max(not_take, take)

    def tabular(self, N, W, val, wt):
        dp = [[0 for x in range(W + 1)] for x in range(N)]

        for i in range(wt[0], W + 1):
            dp[0][i] = (i // wt[0]) * val[0]

        for ind in range(1, N):
            for weig in range(W + 1):
                nott = 0 + dp[ind - 1][weig]
                take = int(-1e9)
                if wt[ind] <= weig:
                    take = val[ind] + dp[ind][weig - wt[ind]]

                dp[ind][weig] = max(take, nott)
        return dp[N - 1][W]
    def knapSack(self, N, W, val, wt):
        # dp = {}
        # return self.dfs(N-1, W, val, wt, dp)
        return self.tabular(N, W, val, wt)

solve = Solution()
print(solve.knapSack(N=2, W=3, val=[1, 1], wt=[2, 1]))