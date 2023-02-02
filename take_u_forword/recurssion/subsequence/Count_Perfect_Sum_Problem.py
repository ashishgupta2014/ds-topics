"""
https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1
"""
class Solution:

    def dfs(self, arr, k, i, dp):
        if k == 0:
            return 1
        if i >= len(arr) or k < 0:
            return 0
        if dp[i][k] != -1:
            return dp[i][k]
        count = self.dfs(arr, k-arr[i], i+1, dp)
        count += self.dfs(arr, k, i+1, dp)
        dp[i][k] = count
        return count
    def perfectSum(self, arr, n, k):
        arr.sort()
        dp = [[-1]*(k+1) for _ in range(n+1)]
        return self.dfs(arr, k, 0, dp) % 1000000007

solve = Solution()
print(solve.perfectSum(arr=[2, 3, 5, 6, 8, 10], n=6, k=10))
print(solve.perfectSum(arr=[1, 2, 3, 4, 5], n=5, k=10))
print(solve.perfectSum(arr=[1, 0], n=2, k=1))