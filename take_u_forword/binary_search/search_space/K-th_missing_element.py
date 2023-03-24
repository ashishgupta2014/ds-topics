"""
https://leetcode.com/problems/kth-missing-positive-number/description/

https://practice.geeksforgeeks.org/problems/k-th-missing-element3635/1

https://www.youtube.com/watch?v=Nfu-ubvJaZ0
"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 1
        high = len(arr)-1
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] - (mid+1) < k:
                low = mid+1
            else:
                high = mid-1
        return high+k+1


solve = Solution()
print(solve.findKthPositive(arr=[2,3,4,7,11], k=5))
