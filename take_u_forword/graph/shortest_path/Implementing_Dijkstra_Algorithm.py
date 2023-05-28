"""
https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

https://www.youtube.com/watch?v=rp1SMw7HSO8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=36

https://takeuforward.org/data-structure/g-35-print-shortest-path-dijkstras-algorithm/
"""
import heapq
from collections import defaultdict


class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        graph = defaultdict(list)
        edges = len(adj)
        for v in range(V):
            if edges > 0:
                for n, w in adj[v]:
                    graph[v].append((n, w))
            edges -= 1
        queue = [(S, 0)]
        heapq.heapify(queue)
        dist_arr = [float('inf')]*V
        dist_arr[S] = 0
        while queue:
            node, dist = heapq.heappop(queue)
            for n, w in graph[node]:
                cur_dist = dist+w
                if dist_arr[n] > cur_dist:
                    dist_arr[n] = cur_dist
                    heapq.heappush(queue, (n, cur_dist))
        dist_arr = [-1 if i == float('inf') else i for i in dist_arr ]
        return dist_arr



solve = Solution()
print(solve.dijkstra(V=3, adj=[[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], S=2))

class Solution2:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        graph = defaultdict(list)
        edges = len(adj)
        for v in range(V):
            if edges > 0:
                for n, w in adj[v]:
                    graph[v].append((n, w))
            edges -= 1
        queue = set()
        queue.add((S, 0))
        dist_arr = [float('inf')]*V
        dist_arr[S] = 0
        while queue:
            node, dist = queue.pop()
            for n, w in graph[node]:
                cur_dist = dist+w
                if dist_arr[n] > cur_dist:
                    dist_arr[n] = cur_dist
                    queue.add((n, cur_dist))
        dist_arr = [-1 if i == float('inf') else i for i in dist_arr ]
        return dist_arr

solve = Solution2()
print(solve.dijkstra(V=3, adj=[[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], S=2))