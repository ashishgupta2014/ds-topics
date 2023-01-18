"""
https://workat.tech/problem-solving/topics/graphs/practice


"""
from typing import List


class Solution:

    directions = [[-1, 0],
                  [0, -1], [0, 1],
                  [1, 0]]

    def dfs(self, image, row, col, source, target):
        if  0 > row or row >= len(image) or 0 > col or col >= len(image[0]):
            return
        if image[row][col] != source:
            return
        image[row][col] = target
        for r, c in self.directions:
            self.dfs(image, row+r, col+c, source, target)

    def applyFloodFill(self, image: List[List[int]], x: int, y: int, c: int) -> List[List[int]]:
        source = image[x][y]
        self.dfs(image, x, y, source, c)
        return image

solve = Solution()

print(solve.applyFloodFill(image=[[1, 0], [0, 0]], x=1, y=1, c=2))

print(solve.applyFloodFill(image=[[1, 1, 0], [1, 1, 1], [1, 1, 1]], x=0, y=0, c=3))

print(solve.applyFloodFill(image=[[1, 2, 1, 2], [2, 2, 2, 1], [1, 2, 2, 1], [2, 1, 2, 1]], x=0, y=1, c=3))

print(solve.applyFloodFill(image=[[1, 2], [2, 1]], x=0, y=1, c=3))