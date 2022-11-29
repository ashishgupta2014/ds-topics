"""
https://workat.tech/problem-solving/practice/trapped-rain-water
"""


class Solution:
    def volumeOfTrappedRainWater(self, heights) -> int:
        n = len(heights)
        left = [0] * n
        right = [0] * n
        left[0] = heights[0]
        right[n - 1] = heights[n - 1]
        for i in range(1, n):
            left[i] = max(left[i - 1], heights[i])

        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], heights[i])

        water = 0

        for i in range(1, n - 1):
            if left[i] <= right[i]:
                water += left[i] - heights[i]
            else:
                water += right[i] - heights[i]
        return water


solve = Solution()
A = [1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solve.volumeOfTrappedRainWater(A))
