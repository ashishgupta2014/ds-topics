"""
https://workat.tech/problem-solving/practice/matrix-search
"""
class Solution:
    def searchMatrix(self, matrix, key: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == key:
                return True
            elif matrix[row][col] < key:
                row += 1
            else:
                col -= 1
        return False




solve = Solution()

mat = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
key = 6
print(solve.searchMatrix(mat, key))