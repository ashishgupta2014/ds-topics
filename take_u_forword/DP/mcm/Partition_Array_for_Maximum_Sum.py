"""
https://leetcode.com/problems/partition-array-for-maximum-sum/description/

https://www.youtube.com/watch?v=PhWWJmaKfMc
"""
from typing import List


class Solution:

    def dfs(self, arr, i, k, dp):
        if i in dp:
            return dp[i]
        if i >= len(arr):
            return 0
        length = 0
        max_num = float('-inf')
        max_sum = 0
        for j in range(i, min(len(arr), i+k)):
            length += 1
            max_num = max(max_num, arr[j])
            cur_sum = length * max_num + self.dfs(arr, j+1, k, dp)
            max_sum = max(max_sum, cur_sum)
        dp[i] = max_sum
        return max_sum
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        return self.dfs(arr, 0, k, {})

solve = Solution()
print(solve.maxSumAfterPartitioning(arr=[1,15,7,9,2,5,10], k=3))