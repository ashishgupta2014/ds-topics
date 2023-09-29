"""
https://leetcode.com/problems/single-number/
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            s ^= n
        return s

solve = Solution()
print(solve.singleNumber(nums=[4,1,2,1,2]))