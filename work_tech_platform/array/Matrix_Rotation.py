class Solution:
    # def rotateMatrix(self, matrix):
    #     n = len(matrix)
    #     rows = n - 1
    #     for i in range(n // 2):
    #         for j in range(i, rows - i):
    #             temp = matrix[j][rows - i]
    #             matrix[j][rows - i] = matrix[i][j]
    #             matrix[i][j] = matrix[rows - j][i]
    #             matrix[rows - j][i] = matrix[rows - i][rows - j]
    #             matrix[rows - i][rows - j] = temp
    #     return matrix

    def rotateMatrix(self, mat):

        # reversing the matrix
        for i in range(len(mat)):
            mat[i].reverse()

        # make transpose of the matrix
        for i in range(len(mat)):
            for j in range(i, len(mat)):
                # swapping mat[i][j] and mat[j][i]
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        return mat


solve = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(solve.rotateMatrix(matrix))
