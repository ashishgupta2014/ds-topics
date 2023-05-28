"""
https://leetcode.com/problems/number-of-enclaves/

https://takeuforward.org/graph/number-of-enclaves/
"""
from typing import List


class Solution:
    def dfs(self, board, row, col):
        if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 1:
            board[row][col] = 2
            self.dfs(board, row-1, col)
            self.dfs(board, row+1, col)
            self.dfs(board, row, col-1)
            self.dfs(board, row, col+1)
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            if grid[row][0] == 1:
                self.dfs(grid, row, 0)
            if grid[row][cols - 1] == 1:
                self.dfs(grid, row, cols - 1)

        for col in range(cols):
            if grid[0][col] == 1:
                self.dfs(grid, 0, col)
            if grid[rows - 1][col] == 1:
                self.dfs(grid, rows - 1, col)
        count = 0
        for row in range(1, rows-1):
            for col in range(1, cols-1):
                if grid[row][col] == 1:
                    count += 1
        return count


solve = Solution()
print(solve.numEnclaves(grid=[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(solve.numEnclaves(grid=[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))