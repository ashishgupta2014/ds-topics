"""
https://practice.geeksforgeeks.org/problems/geek-jump/

https://takeuforward.org/data-structure/dynamic-programming-frog-jump-dp-3/

https://www.youtube.com/watch?v=EgG3jsGoPvQ
"""
import sys


class Solution:

    def dfs(self, height, i, dp):
        if i <= 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        right = sys.maxsize
        left = self.dfs(height, i-1, dp) + abs(height[i]-height[i-1])
        if i > 1:
            right = self.dfs(height, i-2, dp) + abs(height[i]-height[i-2])
        dp[i] = min(left, right)
        return dp[i]

    def tabular(self, n, height, dp):
        dp[0] = 0
        for i in range(1, n):
            left = dp[i-1] + abs(height[i-1]-height[i])
            right = sys.maxsize
            if i > 1:
                right = dp[i-2] + abs(height[i-2]-height[i])
            dp[i] = min(left, right)
        return dp[n-1]

    def two_pointer(self, n, height):
        prev1 = prev2 = 0
        for i in range(1, n):
            jump1 = prev1+abs(height[i-1]-height[i])
            jump2 = sys.maxsize
            if i > 1:
                jump2 = prev2+abs(height[i-2]-height[i])
            cur = min(jump1, jump2)
            prev2 = prev1
            prev1 = cur
        return prev1


    def minimumEnergy(self, height, n):
        # dp = [-1]*n
        # return self.dfs(height, n-1, dp)
        # return self.tabular(n, height, dp)
        return self.two_pointer(n, height)

solve = Solution()
print(solve.minimumEnergy(height=[10, 20, 30, 10], n=4))
