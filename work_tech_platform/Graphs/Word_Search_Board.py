"""
https://workat.tech/problem-solving/practice/word-search-board

"""
from typing import List


class Solution:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(self, board, row, col, word, i):
        if 0 > row or row >= len(board) or 0 > col or col >= len(board[0]) or board[row][col] != word[i]:
            return False
        if i == len(word)-1:
            return True
        i += 1
        for a, b in self.directions:
            if self.dfs(board, row+a, col+b, word, i):
                return True
        return False

    def wordExists(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and self.dfs(board, row, col, word, 0):
                    return True
        return False


solve = Solution()
print(solve.wordExists(board=[['A', 'W', 'O', 'R'], ['T', 'E', 'R', 'K'], ['T', 'A', 'K', 'A']], word='WORKAT'))
print(solve.wordExists(board=[['A', 'W', 'O', 'R'], ['T', 'E', 'R', 'K'], ['T', 'A', 'K', 'A']], word='ATTECH'))



