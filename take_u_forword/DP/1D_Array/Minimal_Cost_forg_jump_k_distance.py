"""
https://practice.geeksforgeeks.org/problems/minimal-cost/1

https://www.youtube.com/watch?v=Kmh3rhyEtB8
"""
import sys


class Solution:

    def dfs(self, height, n, k, dp):
        if n <= 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        min_jumps = sys.maxsize
        for j in range(1, k+1):
            if n-j >= 0:
                jumps = self.dfs(height, n-j, k, dp) + abs(height[n]-height[n-j])
                min_jumps = min(min_jumps, jumps)
        dp[n] = min_jumps
        return min_jumps

    def tabular(self, height, n, k):
        dp = [-1]*n
        dp[0] = 0
        for i in range(1, n):
            min_jumps = sys.maxsize
            for j in range(1, k+1):
                if (i-j) >= 0:
                    jumps = dp[i-j] + abs(height[i] - height[i - j])
                    min_jumps = min(min_jumps, jumps)
            dp[i] = min_jumps
        return dp[n-1]

    def minimizeCost(self, height, n, k):
        # dp = [-1]*n
        # return self.dfs(height, n-1, k, dp)
        return self.tabular(height, n, k)

solve = Solution()
print(solve.minimizeCost(height=[10, 30, 40, 50, 20], n=5, k=3))