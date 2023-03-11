"""
https://leetcode.com/problems/max-consecutive-ones/description/
"""
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        right = 0
        left = 0
        while right < len(nums):
            if nums[right] == 0:
                left = right+1
            else:
                count = max(count, right-left+1)
            right += 1
        return count

solve = Solution()
print(solve.findMaxConsecutiveOnes(nums=[1,1,0,1,1,1]))
print(solve.findMaxConsecutiveOnes(nums=[1,0,1,1,0,1]))