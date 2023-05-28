"""
https://practice.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1

https://takeuforward.org/data-structure/g-35-print-shortest-path-dijkstras-algorithm/
"""
from collections import defaultdict
import heapq


class Solution:
    def shortestPath(self, n, m, edges):
        # Code here
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        queue = []
        heapq.heappush(queue, [0, 1])
        dist = [float('inf') for _ in range(n + 1)]
        dist[1] = 0
        par = [i for i in range(n + 1)]
        while queue:
            dis, node = heapq.heappop(queue)
            for adjnode, weight in graph[node]:
                if dist[adjnode] > weight + dis:
                    dist[adjnode] = weight + dist[node]
                    heapq.heappush(queue, [dist[adjnode], adjnode])
                    par[adjnode] = node

        if dist[n] == float('inf'):
            return [-1]
        path = []
        node = n
        while par[node] != node:
            path.append(node)
            node = par[node]
        path.append(1)
        return path[::-1]



solve = Solution()
print(solve.shortestPath(n=5, m=6, edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]))