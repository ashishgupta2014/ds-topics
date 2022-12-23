"""
https://workat.tech/problem-solving/practice/rat-in-maze
"""
class Solution:
    directions = [(1, 0), (0, 1)]
    rows = 100
    cols = 100
    maze = [[]]

    def move(self, row, col):
        if self.rows == row and self.cols == col:
            return True
        elif self.rows < row or self.cols < col or self.maze[row][col] == 0:
            return False
        for r, c in self.directions:
            if self.move(row + r, col + c):
                return True
        return False

    def canGetCheese(self, maze) -> bool:
        self.rows = len(maze) - 1
        self.cols = len(maze[0]) - 1
        self.maze = maze
        return self.move(0, 0)


solve =  Solution()
maze = [[1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1]]
print(solve.canGetCheese(maze))

maze = [[1, 0, 1, 1, 1],
[1, 1, 1, 0, 1],
[0, 1, 0, 0, 1],
[0, 1, 1, 0, 1]]

print(solve.canGetCheese(maze))