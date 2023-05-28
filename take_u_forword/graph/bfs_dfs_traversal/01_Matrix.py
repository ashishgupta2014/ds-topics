"""
https://leetcode.com/problems/01-matrix/description/

https://takeuforward.org/graph/distance-of-nearest-cell-having-1/
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        visited = [[False]*cols for _ in range(rows)]

        queue = []

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    visited[row][col] = True

        while queue:
            row, col = queue.pop(0)
            directions = [(row+1, col),
                          (row-1, col),
                          (row, col+1),
                          (row, col-1)]
            for r, c in directions:
                if 0 <= r < rows and 0 <= c < cols and visited[r][c] == False:
                    mat[r][c] = 1 + mat[row][col]
                    visited[r][c] = True
                    queue.append((r, c))
        return mat

solve = Solution()
print(solve.updateMatrix(mat=[[0,0,0],[0,1,0],[1,1,1]]))