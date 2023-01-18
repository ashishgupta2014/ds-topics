"""
https://workat.tech/problem-solving/practice/capture-surrounded-regions

https://workat.tech/problem-solving/approach/csr/capture-surrounded-regions

https://www.youtube.com/watch?v=BtdgAys4yMk
"""
from typing import List


class Solution:
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    def dfs(self, board, visited, row, col):
        rows = len(board)
        cols = len(board[0])

        if 0 > row or row >= rows or 0 > col or col >= cols or board[row][col] == 'X' or visited[row][col]:
            return

        visited[row][col] = True
        for r, c in self.directions:
            self.dfs(board, visited, row+r, col+c)

    def getFinalBoard(self, board: List[List[str]]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0])
        visited = [[False]*cols for _ in range(rows)]
        for col in range(cols):
            if board[0][col] == 'O':
                self.dfs(board, visited, 0, col)
            if board[rows-1][col] == 'O':
                self.dfs(board, visited, rows-1, col)
        for row in range(rows):
            if board[row][0] == 'O':
                self.dfs(board, visited, row, 0)
            if board[row][cols-1] == 'O':
                self.dfs(board, visited, row, cols-1)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and not visited[row][col]:
                    board[row][col] = 'X'
        return board

solve = Solution()
board = solve.getFinalBoard(board=[['X', 'X', 'X', 'X', 'X'],
                                 ['X', 'X', 'O', 'O', 'X'],
                                 ['X', 'O', 'X', 'O', 'X'],
                                 ['X', 'O', 'X', 'X', 'X']])
for row in board:
    print(row)



