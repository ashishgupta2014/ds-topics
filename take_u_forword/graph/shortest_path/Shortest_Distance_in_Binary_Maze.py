"""
https://practice.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1

https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

https://www.youtube.com/watch?v=U5Mw4eyUmw4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=37
"""
import heapq
from typing import List


class Solution:

    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        if source == destination:
            return 0
        queue = [(0, source)]
        heapq.heapify(queue)
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dist_arr = [[float('inf')]*cols for _ in range(rows)]
        while queue:
            wt, cell = heapq.heappop(queue)
            row = cell[0]
            col = cell[1]
            for a, b in directions:
                r = row+a
                c = col+b
                if 0 <= r < rows and 0 <= c < cols and grid[r][c]:
                    cur_dist = 1 + wt
                    if dist_arr[r][c] > cur_dist:
                        dist_arr[r][c] = cur_dist
                        heapq.heappush(queue, (cur_dist, [r, c]))

        return -1 if dist_arr[destination[0]][destination[1]] == float('inf') else dist_arr[destination[0]][destination[1]]


solve = Solution()
print(solve.shortestPath(grid= [[1, 1, 1, 1],
                                [1, 1, 0, 1],
                                [1, 1, 1, 1],
                                [1, 1, 0, 0],
                                [1, 0, 0, 1]], source=[0, 1], destination=[2, 2]))