"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

https://takeuforward.org/data-structure/longest-increasing-subsequence-dp-41/

https://takeuforward.org/data-structure/printing-longest-increasing-subsequence-dp-42/

https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1
"""
from typing import List


class Solution:

    def dfs(self, nums, i, prev, dp):
        if i >= len(nums):
            return 0
        if (i, prev) in dp:
            return dp[(i, prev)]

        not_take = self.dfs(nums, i+1, prev, dp)
        take = 0
        if prev == -1 or nums[i] > nums[prev]:
            take = 1 + self.dfs(nums, i+1, i, dp)
        dp[(i, prev)] = max(take, not_take)
        return max(take, not_take)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.dfs(nums, 0, -1, {})
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for prev in range(i+1):
                if nums[i] > nums[prev]:
                    dp[i] = max(dp[i], 1 + dp[prev])
        return max(dp)

solve = Solution()
print(solve.lengthOfLIS(nums=[10,9,2,5,3,7,101,18]))
