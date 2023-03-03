"""
https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1

https://www.youtube.com/watch?v=ZHyb-A2Mte4
"""
class Solution:

    def dfs(self, arr, n, k, dp):
        if k == 0:
            return 1
        if n >= len(arr) or k <0:
            return 0
        if (n, k) in dp:
            return dp[(n, k)]
        take = self.dfs(arr, n + 1, k - arr[n], dp)
        not_take = self.dfs(arr, n + 1, k, dp)
        dp[(n, k)] = take + not_take
        return take + not_take

    def tabular(self, arr, n, k):
        dp = [[0]*(k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        if arr[0] <= k:
            dp[0][arr[0]] = 1
        for ind in range(1, n):
            for target in range(k+1):
                not_take = dp[ind-1][target]
                take = 0
                if arr[ind] <= target:
                    take = dp[ind-1][target-arr[ind]]
                dp[ind][target] = not_take + take
        return dp[-1][k]
    def perfectSum(self, arr, n, k):
        # dp = {}
        # return self.dfs(arr, 0, k, dp) % 1000000007
        return self.tabular(arr, n, k) % 1000000007


solve = Solution()
print(solve.perfectSum(arr=[2, 3, 5, 6, 8, 10], n=6, k=10))
print(solve.perfectSum(arr=[1, 2, 3, 4, 5], n=5, k=10))
print(solve.perfectSum(arr=[9, 7, 0, 3, 9, 8, 6, 5, 7, 6], n=10, k=31))