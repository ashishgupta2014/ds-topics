"""
https://workat.tech/problem-solving/practice/max-path-sum-matrix

https://www.geeksforgeeks.org/maximum-path-sum-matrix/
"""
from typing import List


class Solution:
    def findMaxPath(self, M: List[List[int]]) -> int:

        rows = len(M)
        cols = len(M[0])
        res = 0
        for row in range(1, rows):
            res = 0
            for col in range(cols):
                # Mid elements
                if 0 < col < cols-1:
                    M[row][col] += max(M[row-1][col], M[row-1][col-1], M[row-1][col+1])

                # right corner elements
                elif col > 0:
                    M[row][col] += max(M[row-1][col], M[row-1][col-1])

                # left corner elements
                else:
                    M[row][col] += max(M[row-1][col], M[row-1][col+1])
                res = max(res, M[row][col])
        return res

solve = Solution()

mat = [[12, 22,  5,  0, 20, 18],
        [0,  2,  5, 25, 18, 17],
       [12, 10,  5,  4,  2,  1],
        [3,  8,  2, 20, 10,  8]]
print(solve.findMaxPath(M=mat))

mat = [[1, 1, 1],
       [1, 0, 1],
       [1, 1, 1]]
print(solve.findMaxPath(M=mat))