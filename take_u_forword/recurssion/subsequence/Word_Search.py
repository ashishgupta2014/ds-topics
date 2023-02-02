"""
https://leetcode.com/problems/word-search/description/
"""
from typing import List


class Solution:
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def dfs(self, board, word, row, col):
        if len(word) == 0:
            return True
        rows = len(board)
        cols = len(board[0])

        if row >= rows or 0 > row or col >= cols or 0 > col or board[row][col] != word[0]:
            return False
        temp = board[row][col]
        board[row][col] = '$'

        for x, y in self.directions:
            r = row+x
            c = col+y
            if self.dfs(board, word[1:], r, c):
                return True
        board[row][col] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and self.dfs(board, word, row, col):
                    return True

        return False

solve = Solution()
print(solve.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word='ABCCED'))
print(solve.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word='SEE'))
print(solve.exist(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word='ABCB'))