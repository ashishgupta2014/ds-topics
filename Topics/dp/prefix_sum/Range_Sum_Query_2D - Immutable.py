"""
https://leetcode.com/problems/range-sum-query-2d-immutable/?envType=study-plan&id=dynamic-programming-i

https://www.youtube.com/watch?v=KE8MQuwE2yA
"""


class NumMatrix:

    def __init__(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix += matrix[row][col]

                above = self.dp[row][col + 1]

                self.dp[row + 1][col + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.dp[row2][col2]

        above = self.dp[row1 - 1][col2]

        left = self.dp[row2][col1 - 1]

        topleft = self.dp[row1 - 1][col1 - 1]

        return bottomRight - above - left + topleft


# Your NumMatrix object will be instantiated and called as such:
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
op = [[2, 1, 4, 3],
      [1, 1, 2, 2],
      [1, 2, 2, 4]]
matrix = [[3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)

params = [None]
for row1, col1, row2, col2 in op:
    params.append(obj.sumRegion(row1, col1, row2, col2))

print(params)
