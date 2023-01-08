"""
https://workat.tech/problem-solving/practice/climbing-stairs

"""
class Solution:
    dp = [-1]*50
    dp[1] = 1
    dp[2] = 2
    def backtracking(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.dp[n] != -1:
            return self.dp[n]
        self.dp[n] = self.backtracking(n - 1) + self.backtracking(n - 2)
        return self.dp[n]

    def climbStairs(self, n: int) -> int:
        self.backtracking(n + 1)
        return self.dp[n]



solve = Solution()
print(solve.climbStairs(2))
print(solve.climbStairs(3))
print(solve.climbStairs(4))
print(solve.climbStairs(5))
print(solve.climbStairs(8))