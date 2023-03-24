"""
https://leetcode.com/problems/koko-eating-bananas/description/

https://www.youtube.com/watch?v=U2SozAs9RzA
"""
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = float('inf')
        while low <= high:
            mid = low + (high-low)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/mid)
            if hours <= h:
                ans = min(ans, mid)
                high = mid-1
            else:
                low = mid+1
        return ans

solve = Solution()
print(solve.minEatingSpeed(piles=[3,6,7,11], h=8))
print(solve.minEatingSpeed(piles=[30,11,23,4,20], h=5))
print(solve.minEatingSpeed(piles=[30,11,23,4,20], h=6))