"""
https://leetcode.com/problems/search-insert-position/description/
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:
            return len(nums)
        elif nums[0] > target:
            return 0
        low = 0
        high = len(nums)
        prev = 0
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
                prev = high
            else:
                low = mid+1
                prev = low
        return prev

solve = Solution()
print(solve.searchInsert(nums=[1,3,5,6], target=2))
print(solve.searchInsert(nums=[1,3], target=2))
