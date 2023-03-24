"""
https://leetcode.com/problems/split-array-largest-sum/description/
https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1 same problem

https://www.youtube.com/watch?v=gYmWHvRHu-s&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=69
"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        elif k == 1:
            return sum(nums)
        low = 1
        high = sum(nums)
        res = float('inf')
        while low <= high:
            mid = low+(high-low)//2
            if self.is_possible(mid, nums, k):
                res = min(res, mid)
                high = mid-1
            else:
                low = mid+1
        return res

    def is_possible(self, mid, nums, k):
        s = 0
        count = 1
        for i in range(len(nums)):
            if nums[i] > mid:
                return False
            s += nums[i]
            if s > mid:
                count += 1
                s = nums[i]
        if count > k:
            return False
        return True

solve = Solution()
print(solve.splitArray(nums=[7,2,5,10,8], k=2))