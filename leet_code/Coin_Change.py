class Solution:
    def coinChange(self, coins, amount: int):
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[amount] if dp[amount] != float('inf') else -1


solve = Solution()
# coins = [5, 1, 2]
# amount = 11
coins = [1, 3, 4, 5]
amount = 7
print(solve.coinChange(coins, amount))
