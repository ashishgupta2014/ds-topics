"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/solutions/1581292/well-explained-thought-process-94-faster/
"""
from typing import List


class Solution:

    def is_possible(self, capacity, weights, days):
        total = 0
        d = 1
        for w in weights:
            total += w
            if total > capacity:
                d += 1
                total = w
            if d > days:
                return False
        return True
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = low + (high-low)//2

            if self.is_possible(mid, weights, days):
                high = mid
            else:
                low = mid+1
        return low

solve = Solution()
print(solve.shipWithinDays(weights=[1,2,3,4,5,6,7,8,9,10], days=5))