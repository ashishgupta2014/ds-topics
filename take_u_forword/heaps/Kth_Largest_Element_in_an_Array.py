"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k-1):
            -heapq.heappop(nums)
        return -heapq.heappop(nums)

solve = Solution()
print(solve.findKthLargest(nums=[3,2,1,5,6,4], k=2))