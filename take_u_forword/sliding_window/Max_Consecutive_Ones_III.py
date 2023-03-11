"""
https://leetcode.com/problems/max-consecutive-ones-iii/description/

"""
from typing import List


class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        left, res = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0 and k:
                k -= 1
            elif nums[right] == 0:
                while nums[left] != 0:
                    left += 1
                left += 1
            res = max(res, right - left + 1)
        return res



solve = Solution()
print(solve.longestOnes(nums=[1,1,1,0,0,0,1,1,1,1,0], k=2))
print(solve.longestOnes(nums=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k=3))