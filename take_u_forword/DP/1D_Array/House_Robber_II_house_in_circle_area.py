"""
https://leetcode.com/problems/house-robber-ii/

https://www.youtube.com/watch?v=3WaxQMELSkw
"""
from typing import List


class Solution:

    def two_pointer(self, arr):
        prev1 = prev2 = arr[0]
        n = len(arr)
        for i in range(1, n):
            left = arr[i] if i - 2 < 0 else arr[i] + prev2
            right = prev1
            cur = max(left, right)
            prev2 = prev1
            prev1 = cur
        return prev1
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.two_pointer(nums[:-1]), self.two_pointer(nums[1:]))

solve = Solution()
print(solve.rob(nums=[1,2,3,1]))