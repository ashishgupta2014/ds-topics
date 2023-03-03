"""
https://leetcode.com/problems/partition-equal-subset-sum/description/

https://www.youtube.com/watch?v=7win3dcgo3k
"""
from typing import List


class Solution:

    def dfs(self, nums, n, k, dp):
        if k == 0:
            return True
        if (n, k) in dp:
            return dp[(n, k)]
        if n < 0 or k < 0:
            return False
        take = self.dfs(nums, n-1, k-nums[n], dp)
        not_take = self.dfs(nums, n-1, k, dp)
        dp[(n, k)] = take or not_take
        return take or not_take

    def tabular(self, nums, k):
        n = len(nums)
        dp = [[False]*(k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= k:
            dp[0][nums[0]] = True

        for ind in range(1, n):
            for target in range(1, k+1):
                not_take = dp[ind-1][target]
                take = False
                if nums[ind] <= target:
                    take = dp[ind-1][target-nums[ind]]
                dp[ind][target] = take or not_take
        return dp[n-1][k]

    def canPartition(self, nums: List[int]) -> bool:
        k = sum(nums)
        if k % 2 == 0:
            k //= 2
            # dp = {}
            # return self.dfs(nums, len(nums)-1, k, dp)
            return self.tabular(nums, k)
        return False

solve = Solution()
print(solve.canPartition(nums=[1,5,11,5]))
print(solve.canPartition(nums=[1,2,3,5]))
