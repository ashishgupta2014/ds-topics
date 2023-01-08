"""
https://workat.tech/problem-solving/practice/rod-cutting

https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
https://www.youtube.com/watch?v=mO8XpGoJwuo

"""
from typing import List


class Solution:

    def backtrack(self, n, prices, i, dp):
        if i == 0:
            return prices[i]*n
        if dp[i][n] != -1:
            return dp[i][n]
        # not take
        not_include = 0 + self.backtrack(n, prices, i-1, dp)
        # take it
        included = 0
        if i+1 <= n:
            included = prices[i] + self.backtrack(n-i-1, prices, i, dp)
        dp[i][n] = max(not_include, included)
        return dp[i][n]
    def maximumProfit(self, n: int, prices: List[int]) -> int:
        # dp = [[-1]*(n+1) for _ in range(n+1)]
        # return self.backtrack(n, prices, len(prices)-1, dp)

        # dp = [[0]*(n+1) for _ in range(n+1)]
        #
        # for i in range(n+1):
        #     dp[0][i] = prices[0]*i
        #
        # for row in range(1, n+1):
        #     for col in range(1, n+1):
        #         not_include = 0 + dp[row-1][col]
        #         included = 0
        #         if row+1 <= col:
        #             included = prices[row]+dp[row][col-row-1]
        #         dp[row][col] = max(not_include, included)
        # return dp[-1][-1]
        dp = [0 for _ in range(n + 1)]
        dp[0] = 0

        # Build the table val[] in bottom up manner and return
        # the last entry from the table
        for i in range(1, n + 1):
            max_val = float('-inf')
            for j in range(i):
                max_val = max(max_val, prices[j] + dp[i - j - 1])
            dp[i] = max_val

        return dp[n]


solve = Solution()
print(solve.maximumProfit(n=8, prices=[1, 3, 4, 5, 7, 9, 10, 11]))

print(solve.maximumProfit(n=6, prices=[3, 5, 8, 10, 14, 15]))

print(solve.maximumProfit(n=7, prices=[2, 8, 11, 14, 15, 19, 21]))


