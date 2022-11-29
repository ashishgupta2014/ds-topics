"""
https://leetcode.com/problems/minimum-falling-path-sum/
"""
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        grid = matrix.copy()
        n = len(matrix)
        for row in range(1, n):
            for col in range(n):
                if col == 0:
                    grid[row][col] += min(matrix[row - 1][col], matrix[row - 1][col + 1])
                elif col == n - 1:
                    grid[row][col] += min(matrix[row - 1][col], matrix[row - 1][col - 1])
                else:
                    grid[row][col] += min(matrix[row - 1][col], matrix[row - 1][col - 1], matrix[row - 1][col + 1])
        return min(grid[-1])


solve = Solution()

matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
# matrix = [[100, -42, -46, -41],
#           [31, 97, 10, -10],
#           [-58, -51, 82, 89],
#           [51, 81, 69, -51]]

print(solve.minFallingPathSum(matrix))
