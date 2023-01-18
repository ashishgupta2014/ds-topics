from typing import List


class Solution:
    directions = [[-1, 0],
                  [0, -1], [0, 1],
                  [1, 0]]
    def dfs(self, surface, row, col, visited):
        if 0 > row or 0 > col or row >= len(surface) or col >= len(surface[0]):
            return
        if surface[row][col] and not visited[row][col]:
            visited[row][col] = True
            for x, y in self.directions:
                self.dfs(surface, row+x, col+y, visited)

    def bfs(self, surface, row, col, visited):
        queue = [(row, col)]

        while queue:
            r, c = queue.pop(0)
            visited[r][c] = True
            for x, y in self.directions:
                if 0 <= r + x < len(surface) and 0 <= c + y < len(surface[0]) and surface[r + x][c + y] and not visited[r+x][c+y]:
                    queue.append((r+x, c+y))
    def getNumberOfIslands(self, surface: List[List[int]]) -> int:
        count = 0
        visited = [[False]*len(surface[0]) for _ in range(len(surface))]
        for row in range(len(surface)):
            for col in range(len(surface[0])):
                if surface[row][col] and not visited[row][col]:
                    count += 1
                    # self.dfs(surface, row, col, visited)
                    self.bfs(surface, row, col, visited)
        return count

solve = Solution()
print(solve.getNumberOfIslands(surface=[[1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1]]))



