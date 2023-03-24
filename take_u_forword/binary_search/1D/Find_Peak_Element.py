"""
https://leetcode.com/problems/find-peak-element/description/
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        low = 0
        high = len(nums)-1

        while low <= high:
            mid = low + (high-low)//2
            if mid == 0:
                if nums[mid+1] < nums[mid]:
                    return mid
                elif nums[mid+1] > nums[mid]:
                    return mid+1
            elif mid == len(nums)-1:
                if nums[mid-1] < nums[mid]:
                    return mid
                elif nums[mid - 1] > nums[mid]:
                    return mid-1

            else:
                if nums[mid + 1] < nums[mid] > nums[mid - 1]:
                    return mid
                elif nums[mid-1] < nums[mid] < nums[mid+1]:
                    low = mid+1
                else:
                    high = mid-1
        return low

solve = Solution()
print(solve.findPeakElement(nums=[1,2,1,3,5,6,4]))
print(solve.findPeakElement(nums=[1,2,3,1]))
print(solve.findPeakElement(nums=[1,2,3,4]))
print(solve.findPeakElement(nums=[1]))
print(solve.findPeakElement(nums=[1,2,1,2,1]))
