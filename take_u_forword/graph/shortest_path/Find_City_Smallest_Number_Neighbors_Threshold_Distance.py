"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

https://www.youtube.com/watch?v=PwMVNSJ5SLI
https://takeuforward.org/data-structure/find-the-city-with-the-smallest-number-of-neighbours-at-a-threshold-distance-g-43/
"""
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[1e9]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
        for u, v, d in edges:
            dist[u][v] = d
            dist[v][u] = d

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        city = -1
        cur = 1e9
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1
            if cur > count:
                cur = count
                city = i
            elif cur == count and i > city:
                city = i
        return city



solve = Solution()
print(solve.findTheCity(n=4, edges=[[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold=4))