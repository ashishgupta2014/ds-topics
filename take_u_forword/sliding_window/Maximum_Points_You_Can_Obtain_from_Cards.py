"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

https://www.youtube.com/watch?v=TsA4vbtfCvo
"""
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        left = 0
        right = n-k
        ans = total = sum(cardPoints[right:])

        while right < n:
            total += cardPoints[left] - cardPoints[right]
            ans = max(ans, total)
            left += 1
            right += 1
        return ans

solve = Solution()
print(solve.maxScore(cardPoints=[1,2,3,4,5,6,1], k=3))