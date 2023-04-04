"""
https://leetcode.com/problems/jump-game-ii/description/
"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        temp = 0
        end = 0
        ans = 0
        for i in range(len(nums) - 1):
            end = max(end, i + nums[i])
            if i == temp:
                temp = end
                ans += 1
        return ans

solve = Solution()
print(solve.jump(nums=[2,3,1,1,4]))