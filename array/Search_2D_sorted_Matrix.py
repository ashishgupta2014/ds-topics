class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows = len(matrix) - 1
        cols = len(matrix[0]) - 1
        row = 0
        while row <= rows and cols >= 0:
            if matrix[row][cols] == target:
                return True
            elif matrix[row][cols] < target:
                row += 1
            else:
                cols -= 1
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 23

solve = Solution()
print(solve.searchMatrix(matrix, target))
