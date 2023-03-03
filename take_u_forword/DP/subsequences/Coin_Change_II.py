"""
https://leetcode.com/problems/coin-change-ii/description/

https://www.youtube.com/watch?v=HgyouUi11zk
"""
from typing import List


class Solution:

    def dfs(self, n, amount, coins, dp):
        if n == 0:
            if amount % coins[n] == 0:
                return 1
            return 0
        if (n, amount) in dp:
            return dp[(n, amount)]

        not_take = self.dfs(n-1, amount, coins, dp)
        take = 0
        if coins[n] <= amount:
            take = self.dfs(n, amount-coins[n], coins, dp)
        dp[(n, amount)] = take + not_take
        return take + not_take

    # def tabular(self, amount, coins):
        # has issue
    #     n = len(coins)
    #     dp = [[0]*(amount+1) for _ in range(n)]
    #     for a in range(amount+1):
    #         dp[0][a] = int(amount % coins[0] == 0)
    #
    #     for ind in range(1, n):
    #         for amt in range(amount+1):
    #             not_take = dp[ind-1][amt]
    #             take = 0
    #             if coins[ind] <= amt:
    #                 take = dp[ind][amt-coins[ind]]
    #             dp[ind][amt] = take+not_take
    #     return dp[-1][amount]
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        return self.dfs(len(coins)-1, amount, coins, dp)
        # return self.tabular(amount, coins)

solve = Solution()
print(solve.change(amount=5, coins=[1,2,5]))

print(solve.change(amount=3, coins=[2]))

print(solve.change(amount=4, coins=[1, 2, 3]))

print(solve.change(amount=5, coins=[2, 5]))