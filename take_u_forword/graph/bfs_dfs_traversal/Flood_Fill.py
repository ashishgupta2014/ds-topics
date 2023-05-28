"""
https://leetcode.com/problems/flood-fill/description/
"""
from typing import List


class Solution:
    directions = [
        (0, 1),  # right
        (0, -1),  # left
        (1, 0),  # down
        (-1, 0),  # up
    ]
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        filled = image[sr][sc]
        if filled == color:
            return image
        queue = [(sr, sc)]
        while queue:
            row, col = queue.pop(0)
            image[row][col] = color
            for r, c in self.directions:
                a = row + r
                b = col + c
                if 0 <= a < rows and 0 <= b < cols and image[a][b] == filled:
                    queue.append((a, b))
        return image


solve = Solution()
print(solve.floodFill(image=[[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2))
