"""
This is the Cell class definition

https://workat.tech/problem-solving/practice/knights-journey-chessboard

https://workat.tech/problem-solving/approach/kjc/knights-journey-chessboard

https://www.youtube.com/watch?v=pwlxQeHchFQ
https://www.youtube.com/watch?v=D8KFwjohDNg
"""

class Cell:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    directions = [(-2, -1), (-2, 1), (-1, 2), (-1, -2), (1, -2), (1, 2),(2, -1), (2, 1)]

    def bfs(self, n, board, start, end):
        queue = [(start.x, start.y)]
        board[start.x][start.y] = 0

        while queue:
            x, y = queue.pop(0)
            for a, b in self.directions:
                r = x+a
                c = y+b
                if 0 <= r < n and 0 <= c < n and board[r][c] == -1:
                    board[r][c] = 1 + board[x][y]
                    queue.append((r, c))
        return board[end.x][end.y]

    def minMovesRequired(self, n: int, start: Cell, end: Cell) -> int:
        n += 1
        board = [[-1]*n for _ in range(n)]
        return self.bfs(n, board, start, end)


solve = Solution()

print(solve.minMovesRequired(n=6, start=Cell(6, 1), end=Cell(2, 4)))

print(solve.minMovesRequired(n=2, start=Cell(1, 1), end=Cell(1, 1)))

print(solve.minMovesRequired(n=2, start=Cell(1, 1), end=Cell(2, 2)))

print(solve.minMovesRequired(n=3, start=Cell(3, 3), end=Cell(1, 1)))
