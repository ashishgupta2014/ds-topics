"""
https://leetcode.com/problems/maximal-rectangle/submissions/907695255/

https://www.youtube.com/watch?v=tOylVCugy9k
"""
from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0]*n
        right = [0]*n
        stack = []
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                left[i] = 0
            else:
                left[i] = stack[-1] + 1
            stack.append(i)
        stack = []

        for i in range(n-1, -1, -1):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if len(stack) == 0:
                right[i] = n-1
            else:
                right[i] = stack[-1] - 1
            stack.append(i)
        max_area = 0
        for i in range(n):
            max_area =  max((abs(left[i]-right[i])+1) * heights[i], max_area)
        return max_area
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0]*len(matrix[0])
        max_area = 0
        for row in matrix:
            for i, col in enumerate(row):
                if col == '0':
                    heights[i] = 0
                else:
                    heights[i] += 1
            max_area = max(self.largestRectangleArea(heights=heights), max_area)
        return max_area

solve = Solution()
print(solve.maximalRectangle(matrix=[["1","0","1","0","0"],
                                     ["1","0","1","1","1"],
                                     ["1","1","1","1","1"],
                                     ["1","0","0","1","0"]]))