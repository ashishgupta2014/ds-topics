"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

https://www.youtube.com/watch?v=cKVl1TFdNXg
"""
from typing import List


class Solution:

    def dfs(self, nums, i, prev, count, j):
        if i >= len(nums):
            count[j] = count[j] + 1
            return

        self.dfs(nums, i+1, prev, count, j)
        if prev == -1 or nums[i] > nums[prev]:
            self.dfs(nums, i+1, i, count, j+1)

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # count = [0]*n
        # self.dfs(nums, 0, -1, count, 0)
        # for i in range(n-1, -1, -1):
        #     if count[i] > 0:
        #         return count[i]
        # return 0
        dp = [1]*n
        count = [1]*n
        max_len = 1
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and 1+dp[j] > dp[i]:
                    dp[i] = 1+dp[j]
                    count[i] = count[j]
                elif nums[i] > nums[j] and 1+dp[j] == dp[i]:
                    count[i] += count[j]
            max_len = max(max_len, dp[i])

        possible_lis = 0
        for i in range(n):
            if dp[i] == max_len:
                possible_lis += count[i]
        return possible_lis

solve = Solution()
print(solve.findNumberOfLIS(nums=[1,3,5,4,7]))