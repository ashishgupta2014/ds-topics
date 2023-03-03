"""
https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

https://www.youtube.com/watch?v=fWX9xDmIzRI
"""
class Solution:

    def dfs(self, arr, n, k, dp):
        if k == 0:
            return True
        if n < 0 or k < 0:
            return False
        if (n, k) in dp:
            return dp[(n, k)]
        take = self.dfs(arr, n-1, k-arr[n], dp)
        not_take = self.dfs(arr, n-1, k, dp)
        dp[(n, k)] = take or not_take
        return take or not_take

    def tabular(self, arr, n, k):
        dp = [[False]*(k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        if arr[0] <= k:
            dp[0][arr[0]] = True

        for ind in range(1, n):
            for target in range(1, k+1):
                not_take = dp[ind-1][target]
                take = False
                if arr[ind] <= target:
                    take = dp[ind-1][target-arr[ind]]
                dp[ind][target] = not_take or take
        return dp[n-1][k]
    def isSubsetSum(self, N, arr, k):
        # dp = {}
        # return self.dfs(arr, N-1, k, dp)
        return self.tabular(arr, N, k)

solve = Solution()
print(solve.isSubsetSum(N=6, arr=[3, 34, 4, 12, 5, 2], k=9))
print(solve.isSubsetSum(N=6, arr=[3, 34, 4, 12, 5, 2], k=30))
