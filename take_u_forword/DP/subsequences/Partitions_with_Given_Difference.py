"""
https://practice.geeksforgeeks.org/problems/partitions-with-given-difference/1

https://www.youtube.com/watch?v=zoilQD1kYSg
"""
class Solution:

    def dfs(self, arr, n, k, dp):
        if n == 0:
            if k == 0 and arr[0] == 0:
                return 2
            if k == 0 or arr[0] == k:
                return 1
            return 0
        if (n, k) in dp:
            return dp[(n, k)]
        not_take = self.dfs(arr, n -1, k, dp)
        take = 0
        if arr[n] <= k:
            take = self.dfs(arr, n -1, k - arr[n], dp)

        dp[(n, k)] = take + not_take
        return take + not_take

    def tabular(self, arr, n, k):
        dp = [[0]*(k+1) for _ in range(n)]
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        if arr[0] != 0 and arr[0] <= k:
            dp[0][arr[0]] = 1

        for ind in range(1, n):
            for target in range(k+1):
                not_take = dp[ind-1][target]
                take = 0
                if arr[ind] <= target:
                    take = dp[ind-1][target-arr[ind]]
                dp[ind][target] = not_take + take
        return dp[-1][k]
    def countPartitions(self, n, d, arr):
        dp = {}
        totalSum = sum(arr)
        k = (totalSum - d)//2
        # diff is greater or totalSum odd
        if totalSum < d or (totalSum - d) % 2:
            return 0
        # return self.dfs(arr, n-1, k, dp) % 1000000007
        return self.tabular(arr, n, k) % 1000000007

solve = Solution()
print(solve.countPartitions(n=4, d=3, arr=[5, 2, 6, 4]))
print(solve.countPartitions(n=4, d=0, arr=[1, 1, 1, 1]))
print(solve.countPartitions(n=17, d=2, arr=[2, 40, 6, 6, 43, 44, 10, 32, 12, 12, 26, 31, 48, 14, 38, 42, 25]))