"""
https://leetcode.com/problems/n-queens/submissions/886219747/

https://www.youtube.com/watch?v=i05Ju7AftcM&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=14
"""
from typing import List


class Solution:
    directions = [(0, -1), (-1, -1), (-1, 0), (1, -1)]
    result = []

    def is_safe(self, board, row, col):
        n = len(board)

        for x, y in self.directions:
            r = row
            c = col
            while 0 <= r < n and 0 <= c < n:
                if board[r][c] == 'Q':
                    return False
                r += x
                c += y
        return True

    def dfs(self, board, n, col):
        if col >= n:
            self.result.append([''.join(row) for row in board[:]])
            return True
        for row in range(n):
            if self.is_safe(board, row, col):
                board[row][col] = 'Q'
                self.dfs(board, n, col+1)
                board[row][col] = '.'
        return False
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        board = [['.']*n for _ in range(n)]
        self.dfs(board, n, 0)
        return self.result

solve = Solution()
print(solve.solveNQueens(n=4))