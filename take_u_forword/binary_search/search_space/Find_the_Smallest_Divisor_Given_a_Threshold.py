"""
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
"""
import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        while low < high:
            mid = low + (high-low)//2
            total = self.is_division_possible(mid, nums)
            if total > threshold:
                low = mid+1
            else:
                high = mid
        return low


    def is_division_possible(self, d, nums):
        total = 0
        for n in nums:
            total += math.ceil(n/d)
        return total


solve = Solution()
print(solve.smallestDivisor(nums=[1,2,5,9], threshold=6))
print(solve.smallestDivisor(nums=[44,22,33,11,1], threshold=5))