"""
https://leetcode.com/problems/rotting-oranges/

https://takeuforward.org/data-structure/rotten-oranges/
"""
from typing import List

class Cell:
    def __init__(self, row, col, time=0):
        self.row = row
        self.col = col
        self.time = time


class Solution:
    directions = [
            (0, 1),  # right
            (0, -1),  # left
            (1, 0),  # down
            (-1, 0),  # up
        ]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = [Cell(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == 2]
        time = 0
        while queue:
            cell = queue.pop(0)
            time = cell.time
            for r, c in self.directions:
                row = cell.row + r
                col = cell.col + c
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                    queue.append(Cell(row=row, col=col, time=cell.time+1))
                    grid[row][col] = 2
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return time



solve = Solution()
print(solve.orangesRotting(grid=[[2,1,1],[1,1,0],[0,1,1]]))