class Solution:

    board = []
    directions = [(0, -1),  # left side
                 (-1, -1),  # upper left diagonal
                 (1, -1)  # down left diagonal
                 ]

    def is_queen_safe(self, r, c, n):
        for x, y in self.directions:
            a = r
            b = c
            while 0 <= a < n and 0 <= b < n:
                if self.board[a][b] == 'Q':
                    return False
                a += x
                b += y
        return True


    def backtrack(self, n, col):
        if col >= n:
            return True
        for i in range(n):
            if self.is_queen_safe(i, col, n):
                self.board[i][col] = 'Q'
                if self.backtrack(n, col+1):
                    return True
                self.board[i][col] = '.'
        return False


    def getNQueensSolutions(self, n: int):
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        for row in self.board:
            print(row)
        self.backtrack(n, 0)
        print('---------')
        for row in self.board:
            print(row)
        result = [[''.join(b)] for b in self.board]
        for row in result:
            print(row)
        return result

solve = Solution()
board = solve.getNQueensSolutions(n=1)
for row in board:
    print(row)

board = solve.getNQueensSolutions(n=4)
for row in board:
    print(row)


