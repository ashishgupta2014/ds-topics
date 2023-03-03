"""
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

https://www.youtube.com/watch?v=X0X6G-eWgQ8
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




solve = Solution()
print(solve.largestRectangleArea(heights=[2,1,5,6,2,3]))
