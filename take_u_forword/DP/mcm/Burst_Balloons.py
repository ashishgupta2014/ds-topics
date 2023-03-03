"""
https://leetcode.com/problems/burst-balloons/description/

https://www.youtube.com/watch?v=Yz4LlDSlkns
"""
from typing import List


class Solution:

    def dfs(self, nums, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        if i > j:
            return 0
        max_coins = float('-inf')
        for k in range(i, j+1):
            coins = nums[i-1]*nums[k]*nums[j+1] + self.dfs(nums, i, k-1, dp) + self.dfs(nums, k+1, j, dp)
            max_coins = max(max_coins, coins)
        dp[(i, j)] = max_coins
        return max_coins
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        return self.dfs(nums, 1, len(nums)-2, {})

solve = Solution()
print(solve.maxCoins(nums=[3,1,5,8]))