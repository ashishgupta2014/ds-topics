"""
https://leetcode.com/problems/target-sum/description/

https://www.youtube.com/watch?v=b3GD8263-PQ
"""
from typing import List


class Solution:

    def dfs(self, nums, target, n, dp):
        if n == 0:
            if target == 0 and nums[0] == 0:
                return 2
            if target == 0 or nums[0] == target:
                return 1
            return 0
        if (n, target) in dp:
            return dp[(n, target)]
        not_take = self.dfs(nums, target, n - 1, dp)
        take = 0
        if nums[n] <= target:
            take = self.dfs(nums, target-nums[n], n-1, dp)
        dp[(n, target)] = take + not_take
        return take + not_take

    def tabular(self, arr, k):
        n = len(arr)
        dp = [[0]*(k+1) for _ in range(n)]
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        if arr[0] != 0 and arr[0] <= k:
            dp[0][arr[0]] = 1

        for ind in range(1, n):
            for target in range(k+1):
                not_take = dp[ind-1][target]
                take = 0
                if arr[ind] <= target:
                    take = dp[ind-1][target-arr[ind]]
                dp[ind][target] = not_take + take
        return dp[-1][k]
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        totalSum = sum(nums)
        k = (totalSum - target) // 2
        if totalSum < target or (totalSum - target) % 2:
            return 0

        # return self.dfs(nums, k, len(nums)-1, dp)
        return self.tabular(nums, k)

solve = Solution()
print(solve.findTargetSumWays(nums=[1,1,1,1,1], target=3))