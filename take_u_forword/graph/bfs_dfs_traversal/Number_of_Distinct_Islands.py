"""
https://takeuforward.org/data-structure/number-of-distinct-islands/

https://practice.geeksforgeeks.org/problems/number-of-distinct-islands/1
"""
from typing import List


class Solution:

    def dfs(self, grid, visited, row, col, temp):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] and visited[row][col]:
            visited[row][col] = 0
            temp.append((row, col))
            self.dfs(grid, visited, row-1, col, temp)
            self.dfs(grid, visited, row+1, col, temp)
            self.dfs(grid, visited, row, col-1, temp)
            self.dfs(grid, visited, row, col+1, temp)
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        visited = grid.copy()
        result = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and visited[i][j]:
                    temp = []
                    self.dfs(grid, visited, i, j, temp)
                    result.add(tuple((x-i, y-j) for x, y in temp))
        return len(result)



solve = Solution()
print(solve.countDistinctIslands(grid=[[1, 1, 0, 0, 0],
                                       [1, 1, 0, 0, 0],
                                       [0, 0, 0, 1, 1],
                                       [0, 0, 0, 1, 1]]))