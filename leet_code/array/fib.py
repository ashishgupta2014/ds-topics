dp = [0 for _ in range(30)]


class Solution:
    def fib(self, n: int) -> int:
        s = self.recursive(n)
        return s

    def recursive(self, n):
        if n <= 1:
            return n

        if dp[n] != -1:
            return n
        dp[n] = self.recursive(n - 1) + self.recursive(n - 2)
        return dp[n]


print(Solution().fib(5))
