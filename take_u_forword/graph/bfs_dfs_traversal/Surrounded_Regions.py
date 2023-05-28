"""
https://leetcode.com/problems/surrounded-regions/

https://www.youtube.com/watch?v=BtdgAys4yMk

https://takeuforward.org/graph/surrounded-regions-replace-os-with-xs/
"""
from typing import List


class Solution:

    def dfs(self, board, row, col):
        if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == 'O':
            board[row][col] = 'D'
            self.dfs(board, row-1, col)
            self.dfs(board, row+1, col)
            self.dfs(board, row, col-1)
            self.dfs(board, row, col+1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            if board[row][0] == 'O':
                self.dfs(board, row, 0)
            if board[row][cols-1] == 'O':
                self.dfs(board, row, cols-1)

        for col in range(cols):
            if board[0][col] == 'O':
                self.dfs(board, 0, col)
            if board[rows-1][col] == 'O':
                self.dfs(board, rows-1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'D':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'




solve = Solution()
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
solve.solve(board=board)
print(board)
