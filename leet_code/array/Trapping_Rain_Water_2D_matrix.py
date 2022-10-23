import heapq


class Solution:
    def trapRainWater(self, heightMap):
        rows = len(heightMap)
        cols = len(heightMap[0])
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        queue = [(heightMap[row][col], row, col) for row in range(rows)
                 for col in range(cols)
                 if col == 0 or row == 0 or row == rows - 1 or col == cols - 1]
        visited = [[True if i == 0 or j == 0 or j == rows - 1 or i == cols - 1 else False for i in range(cols)] for j
                    in range(rows)]
        heapq.heapify(queue)
        water = 0
        while queue:
            height, row, col = heapq.heappop(queue)
            for dr, dc in direction:
                nr = dr + row
                nc = dc + col
                if nr < 1 or nr >= rows - 1 or nc < 1 or nc >= cols - 1 or visited[nr][nc] is True:
                    continue
                n_height = heightMap[nr][nc]
                if n_height < height:
                    water += height - n_height
                    heapq.heappush(queue, (height, nr, nc))
                else:
                    heapq.heappush(queue, (heightMap[nr][nc], nr, nc))
                visited[nr][nc] = True
        return water


solve = Solution()
matrix = [[1, 4, 3, 1, 3, 2],
          [3, 2, 1, 3, 2, 4],
          [2, 3, 3, 2, 3, 1]]
print(solve.trapRainWater(matrix))
