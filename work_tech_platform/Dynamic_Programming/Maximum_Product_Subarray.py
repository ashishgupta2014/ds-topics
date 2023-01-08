"""
https://workat.tech/problem-solving/practice/max-product-subarray

https://leetcode.com/problems/maximum-product-subarray/description/

https://www.youtube.com/watch?v=lXVy6YWFcRM

Notes:
    [1, 2, 3, 4....] => Positive numbers gives always highest numbers

    [-1, -2, -3....] =>
        [-1,-2] returns 3
        [-2, -3] returns 6
        [-1, -2, -3] returns -6
        On this reason need to keep track of max and min  both and decide which one has the highest value

    0 => either positive or negative both become zero. whenever zero found need to reset the min and max
"""
from typing import List


class Solution:
    def maxProduct(self, A: List[int]) -> int:
        res = max(A)
        cur_min = cur_max = 1
        for a in A:
            if a == 0:
                cur_min = cur_max = 1
                continue
            tmp = cur_max*a
            cur_max = max(tmp, a*cur_min, a)
            cur_min = min(tmp, a*cur_min, a)
            res = max(cur_max, res)
        return res

solve = Solution()
print(solve.maxProduct(A=[-1, 3, 2, -1, -2, 3, 0, -2]))



