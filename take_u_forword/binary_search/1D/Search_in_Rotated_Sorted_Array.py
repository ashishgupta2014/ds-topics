"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            elif nums[mid] <= target <= nums[high]:
                low = mid+1
            else:
                high = mid-1
        if nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        return -1


solve = Solution()
print(solve.search(nums=[4,5,6,7,0,1,2], target=0))
print(solve.search(nums=[4,5,6,7,0,1,2], target=3))
print(solve.search(nums=[1], target=1))
print(solve.search(nums=[4,5,6,7,0,1,2], target=5))
print(solve.search(nums=[4,5,6,7,0,1,2], target=1))
print(solve.search(nums=[1, 3], target=3))
print(solve.search(nums=[3, 1], target=1))
print(solve.search(nums=[4,5,6,7,0,1,2], target=6))