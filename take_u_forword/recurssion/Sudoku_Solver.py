"""
https://workat.tech/problem-solving/practice/sudoku-solver

https://leetcode.com/problems/sudoku-solver/description/

https://leetcode.com/problems/sudoku-solver/solutions/515350/simple-backtracking-python-solution/?orderBy=most_relevant&languageTags=python3

https://www.youtube.com/watch?v=FWAIf_EVUKE&t=1088s

https://www.youtube.com/watch?v=FWAIf_EVUKE&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=15

"""
class Solution:
    board = []
    possibility = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def is_board_filled(self):
        for row in range(9):
            if '.' in self.board[row]:
                return False
        return True
    def backtracking(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    for p in self.possibility:
                        if self.is_valid(row, col, p):
                            self.board[row][col] = p
                            self.backtracking()
                            if not self.is_board_filled():
                                self.board[row][col] = '.'
                    return

    def is_valid(self, row, col, p):
        if p in self.board[row]:
            return False
        for r in range(9):
            if self.board[r][col] == p:
                return False
        block_row = row//3
        block_col = col//3
        for r in range(3):
            for c in range(3):
                if self.board[block_row*3 + r][block_col*3 + c] == p:
                    return False
        return True

    def solveSudoku(self, sudoku) -> None:
        self.board = sudoku
        self.backtracking()


solve = Solution()

board = [ "2 5 . . . 3 . . .".split(' '),
          ". . . . . . 2 7 .".split(' '),
          "8 7 . . . 6 4 . .".split(' '),
          ". 2 . . . 8 1 9 3".split(' '),
          ". 1 5 . 4 . 8 . .".split(' '),
          ". . . 1 . . . . 4".split(' '),
          ". . . 7 3 4 . . .".split(' '),
          ". . . 6 . . . . 9".split(' '),
          ". 6 4 . . 9 . 5 8".split(' ')]
solve.solveSudoku(board)
for row in board:
    print(row)
