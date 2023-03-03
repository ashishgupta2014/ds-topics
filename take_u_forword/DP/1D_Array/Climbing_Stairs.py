"""
https://leetcode.com/problems/climbing-stairs/description/

https://www.youtube.com/watch?v=mLfjzJsN8us&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=3
"""
class Solution:
    dp = [-1 for _ in range(46)]
    def dfs(self, n):
        if n <= 1:
            return n
        if self.dp[n] != -1:
            return self.dp[n]

        self.dp[n] = self.dfs(n-1)+self.dfs(n-2)
        return self.dp[n]
    def climbStairs(self, n: int) -> int:
        # return self.dfs(n+1)
        prev1 = 1
        prev2 = 1
        for i in range(2, n+1):
            cur = prev1+prev2
            prev2 = prev1
            prev1 = cur
        return prev1

solve = Solution()
print(solve.climbStairs(n=3))
print(solve.climbStairs(n=2))
print(solve.climbStairs(n=5))
print(solve.climbStairs(n=1))
print(solve.climbStairs(n=0))
