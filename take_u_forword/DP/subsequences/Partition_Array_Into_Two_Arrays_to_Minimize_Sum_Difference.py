"""
https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1

https://www.youtube.com/watch?v=GS_OqZb2CWc
"""
from typing import List


class Solution:

    def minimumDifference(self, nums: List[int]) -> int:
        k = sum(nums)
        n = len(nums)
        dp = [[False]*(abs(k)+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if nums[0] <= k:
            dp[0][k] = True

        for ind in range(1, n):
            for target in range(1, k+1):
                not_take = dp[ind-1][target]
                take = False
                if nums[ind] <= target:
                    take = dp[ind-1][target-nums[ind]]
                dp[ind][target] = take or not_take

        min_sum = float('inf')
        for x in range(abs(k)):
            if dp[-1][x]:
                min_sum = min(min_sum, abs(x-(k-x)))
        return min_sum

solve = Solution()
print(solve.minimumDifference(nums=[3,9,7,3]))
print(solve.minimumDifference(nums=[1, 6, 11, 5]))
