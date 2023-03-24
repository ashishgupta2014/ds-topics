"""
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

https://www.youtube.com/watch?v=paYIrQKxE7I
"""
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        low = 1
        high = max(bloomDay)

        while low < high:
            mid = low + (high-low)//2
            no_of_bouquets = self.count_possible_bouquets(mid, bloomDay, k)
            if no_of_bouquets < m:
                low = mid+1
            else:
                high = mid
        return low

    def count_possible_bouquets(self, day, bloomDay, k):
        cnt = 0  # no of bouquets made
        temp = 0
        for i in range(len(bloomDay)):
            if bloomDay[i] > day:
                temp = 0
            else:
                temp += 1
            if temp == k:  # if we got k consecutive days < mid days then we can make 1 more so cnt+=1
                cnt += 1
                temp = 0  # set temp=0 to find another k consecutive days
        return cnt  # return cnt (no of bouquets made)

solve = Solution()
print(solve.minDays(bloomDay=[7,7,7,7,12,7,7], m=2, k=3))