"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

https://www.youtube.com/watch?v=HGtqdzyUJ3k

https://takeuforward.org/data-structure/search-single-element-in-a-sorted-array/
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==nums[mid^1]:
                low=mid+1
            else:
                high=mid-1
        return nums[low]

solve = Solution()
print(solve.singleNonDuplicate(nums=[1,1,2,3,3,4,4,8,8]))