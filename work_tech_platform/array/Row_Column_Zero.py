class Solution:
    def setRowColumnZeroes(self, matrix) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[row][col] = '#'
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == '#':
                    i = 0
                    # row based change
                    matrix[row][col] = 0
                    while i < rows and matrix[i][col] != '#':
                        matrix[i][col] = 0
                        i += 1
                    j = 0
                    # col based change
                    while j < cols and matrix[row][j] != '#':
                        matrix[row][j] = 0
                        j += 1


solve = Solution()
mat = [[1, 1, 0],
       [1, 0, 1],
       [1, 1, 1]]
solve.setRowColumnZeroes(mat)
for row in mat:
    print(row)