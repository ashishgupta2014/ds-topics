"""
https://workat.tech/problem-solving/practice/coin-change

https://practice.geeksforgeeks.org/problems/coin-change2448/1

https://www.youtube.com/watch?v=HgyouUi11zk
"""
from typing import List


class Solution:

    def backtrack(self, coins, target, i):
        if target == 0:
            return 1
        if i < 0 or target < 0:
            return 0
        target -= coins[i]
        ans = self.backtrack(coins, target, i)
        target += coins[i]
        ans += self.backtrack(coins, target, i-1)
        target -= coins[i]
        return ans

    def backtrack_knapsack(self, coins, target, i, dp):
        if i == 0:
            return target % coins[0] == 0

        if dp[i][target] != -1:
            return dp[i][target]

        not_take = self.backtrack_knapsack(coins, target, i-1, dp)
        take = 0

        if coins[i] <= target:
            take = self.backtrack_knapsack(coins, target-coins[i], i, dp)
        dp[i][target] = not_take + take
        return dp[i][target]
    def numberOfCombinations(self, coins: List[int], target: int) -> int:
        # return self.backtrack(coins, target, len(coins)-1)
        # dp = [[-1]*(target+1) for _ in range(len(coins)+1)]
        # return self.backtrack_knapsack(coins, target, len(coins)-1, dp)
        n = len(coins)

        matrix = [[0] * (target + 1) for _ in range(n + 1)]

        matrix[0][0] = 1

        for i in range(1, n + 1):
            matrix[i][0] = 1
            for j in range(1, target + 1):
                if coins[i - 1] > j:
                    matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i - 1][j] + matrix[i][j - coins[i - 1]]

        return matrix[n][target]


solve = Solution()
print(solve.numberOfCombinations(coins=[5, 2, 4], target=13))

print(solve.numberOfCombinations(coins=[2, 5, 4], target=28))

print(solve.numberOfCombinations(coins=[1, 2, 4, 5], target=28))