"""
https://leetcode.com/problems/path-with-minimum-effort/description/

https://www.youtube.com/watch?v=0ytpZyiZFhA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=38

https://takeuforward.org/data-structure/g-37-path-with-minimum-effort/
"""
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        diff_arr = [[float('inf')]*cols for _ in range(rows)]

        queue = [(0, (0, 0))]
        heapq.heapify(queue)
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        diff_arr[0][0] = 0

        while queue:
            d, cell = heapq.heappop(queue)
            row = cell[0]
            col = cell[1]

            for a, b in directions:
                r = row+a
                c = col+b
                if 0 <= r < rows and 0 <= c < cols:
                    new_diff = abs(heights[row][col] - heights[r][c])
                    diff = new_diff if new_diff > d else d
                    if diff < diff_arr[r][c]:
                        diff_arr[r][c] = diff
                        heapq.heappush(queue, (diff, (r, c)))
        return diff_arr[-1][-1]


solve = Solution()
print(solve.minimumEffortPath(heights=[[1,2,2],[3,8,2],[5,3,5]]))