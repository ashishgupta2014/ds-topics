"""
https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1

https://www.youtube.com/watch?v=ZUFQfFaU-8U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=28
"""
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
        dist_arr = [float('inf')]*n
        queue = [(0, 0)]
        dist_arr[0] = 0
        while queue:
            node, dist = queue.pop(0)
            for i in graph[node]:
                n = i[0]
                w = i[1]
                cur_dist = dist+ w
                if dist_arr[n] > cur_dist:
                    queue.append((n, cur_dist))
                    dist_arr[n] = cur_dist
        dist_arr = [-1 if i == float('inf') else i for i in dist_arr]
        return dist_arr

solve = Solution()
print(solve.shortestPath(n=6, m=7,edges=[[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]))