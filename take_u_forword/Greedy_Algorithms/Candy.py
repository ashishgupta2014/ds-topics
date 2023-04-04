"""
https://leetcode.com/problems/candy/description/
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                right[i] = 1 + right[i + 1]

        left = [1] * n

        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                left[i] = 1 + left[i - 1]
        result = 0
        for i in range(n):
            if left[i] < right[i]:
                result += right[i]
            else:
                result += left[i]
        return result

solve = Solution()
print(solve.candy(ratings=[1,2,2]))