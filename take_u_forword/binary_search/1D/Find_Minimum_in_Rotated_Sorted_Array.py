"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        low = 0
        high = n-1
        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[high] > nums[0]:
            return nums[0]

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                low = mid+1
            else:
                high = mid-1
        return nums[low]


solve = Solution()
print(solve.findMin(nums=[3,4,5,1,2]))
