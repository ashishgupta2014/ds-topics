"""
https://leetcode.com/problems/jump-game/description/
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1
        l = n
        for i in range(n, -1, -1):
            if l <= i + nums[i]:
                l = i
        return l==0


solve = Solution()
print(solve.canJump(nums=[2,3,1,1,4]))
