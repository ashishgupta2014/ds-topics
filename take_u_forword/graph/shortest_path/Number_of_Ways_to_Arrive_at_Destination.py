"""
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/

https://www.youtube.com/watch?v=_-0mx0SmYxA&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=41

https://takeuforward.org/data-structure/g-40-number-of-ways-to-arrive-at-destination/
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        queue = [(0, 0)]
        heapq.heapify(queue)
        dist = [float('inf')]*n
        ways = [0]*n
        dist[0] = 0
        ways[0] = 1
        while queue:
            w, u = heapq.heappop(queue)
            for v, t in graph[u]:
                cur = w+t
                if dist[v] > cur:
                    dist[v] = cur
                    ways[v] = ways[u]
                    heapq.heappush(queue, (cur, v))
                elif dist[v] == cur:
                    ways[v] = (ways[u] + ways[v]) %(pow(10,9)+7)
        return ways[-1]



solve = Solution()
print(solve.countPaths(n=7, roads=[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))