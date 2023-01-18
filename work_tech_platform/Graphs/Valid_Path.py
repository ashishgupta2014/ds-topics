"""
This is the Circle class definition
https://workat.tech/problem-solving/approach/vp/valid-path

https://www.youtube.com/watch?v=In6MrAYjeZw

"""
from typing import List

class Circle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y



class Solution:

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    def hasValidPath(self, n: int, m: int, r: int, circles: List[Circle]) -> bool:
        n += 1
        m += 1
        matrix = [[False]*m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                for circle in circles:
                    if (row == circle.x and col == circle.y) or (abs(circle.x-row)**2 + abs(circle.y-col)**2 <= r**2):
                        matrix[row][col] = True
        if matrix[n-1][m-1] or matrix[0][0]:
            return False
        queue = [(0, 0)]


        while queue:
            x, y = queue.pop(0)
            if x == n-1 and y == m-1:
                return True

            matrix[x][y] = True
            for r, c in self.directions:
                row = x+r
                col = y+c
                if 0 <= row < n and 0 <= col < m and not matrix[row][col]:
                    queue.append((row, col))
        return False


solve = Solution()
print(solve.hasValidPath(n=5, m=4, r=1, circles=[Circle(0, 2), Circle(2, 3), Circle(3, 0), Circle(4, 1)]))

print(solve.hasValidPath(n=5, m=4, r=1, circles=[Circle(0, 2), Circle(2, 3), Circle(3, 0), Circle(4, 3)]))



