"""
https://leetcode.com/problems/search-a-2d-matrix/description/
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols-1
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


solve = Solution()
print(solve.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3))
print(solve.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=0))
print(solve.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=1))