"""
https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1

https://www.youtube.com/watch?v=C4gxoTaI71U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=29
"""
from collections import defaultdict


class Solution:
    def shortestPath(self, edges, n, m, src):
        graph  = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = [(src, 0)]
        dist_arr = [float('inf')]*n
        dist_arr[src] = 0
        while queue:
            node, dist = queue.pop(0)
            for v in graph[node]:
                cur_dist = dist+1
                if dist_arr[v] > cur_dist:
                    queue.append((v, cur_dist))
                    dist_arr[v] = cur_dist
        dist_arr = [-1 if i == float('inf') else i for i in dist_arr]
        return dist_arr


solve = Solution()
print(solve.shortestPath(n=9, m=10,edges=[[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]], src=0))