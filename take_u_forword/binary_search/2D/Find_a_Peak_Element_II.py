"""
https://leetcode.com/problems/find-a-peak-element-ii/description/
"""
from typing import List


class Solution:
    def __init__(self):
        self.mat = None
        self.cols = None
        self.rows = None

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.mat = mat
        row, col = 0, 0
        while row < self.rows:
            while col < self.cols:
                if (self.is_valid(row, col - 1) < self.is_valid(row, col)
                        and self.is_valid(row, col) > self.is_valid(row, col + 1)
                        and self.is_valid(row, col) > self.is_valid(row - 1, col)
                        and self.is_valid(row, col) > self.is_valid(row + 1, col)):
                    return [row, col]
                # left
                elif self.is_valid(row, col) < self.is_valid(row, col - 1):
                    col = col - 1
                # right
                elif self.is_valid(row, col) < self.is_valid(row, col + 1):
                    col = col + 1
                # top
                elif self.is_valid(row, col) < self.is_valid(row - 1, col):
                    row = row - 1
                # bottom
                elif self.is_valid(row, col) < self.is_valid(row + 1, col):
                    row = row + 1

    def is_valid(self, row, col) -> int:
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
            return -1
        else:
            return self.mat[row][col]
                    



solve = Solution()
print(solve.findPeakGrid(mat=[[10,20,15],[21,30,14],[7,16,32]]))