"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        return [first, last]

    def findFirst(self, arr, tar):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == tar:
                if mid - 1 >= 0 and arr[mid - 1] != tar or mid == 0:
                    return mid
                right = mid - 1
            elif arr[mid] > tar:
                right = mid - 1
            else:
                left = mid + 1
        return - 1

    def findLast(self, arr, tar):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == tar:
                if mid + 1 < len(arr) and arr[mid + 1] != tar or mid == len(arr) - 1:
                    return mid
                left = mid + 1
            elif arr[mid] > tar:
                right = mid - 1
            else:
                left = mid + 1
        return - 1

solve = Solution()
print(solve.searchRange(nums=[5,7,7,8,8,10], target=8))
