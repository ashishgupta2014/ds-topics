"""
https://leetcode.com/problems/critical-connections-in-a-network/description/

https://takeuforward.org/graph/bridges-in-graph-using-tarjans-algorithm-of-time-in-and-low-time-g-55/

https://www.youtube.com/watch?v=qrAub5z8FeA
"""
from collections import defaultdict
from typing import List


class Solution:
    timer = 1
    def dfs(self, root, parent, visited, adj, tin, low, bridges):
        visited[root] = True
        tin[root] = low[root] = self.timer
        self.timer += 1
        for node in adj[root]:
            if node == parent:
                continue
            if not visited[node]:
                self.dfs(node, root, visited, adj, tin, low, bridges)
                low[root] = min(low[node], low[root])
                if low[node] > tin[root]:
                    bridges.append([node, root])
            else:
                low[root] = min(low[root], low[node])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        tin = [0]*n
        low = [0]*n
        visited = [False]*n
        bridges = []
        self.timer = 1
        self.dfs(0, -1, visited, graph, tin, low, bridges)
        return bridges

solve = Solution()
print(solve.criticalConnections(n=4, connections=[[0,1],[1,2],[2,0],[1,3]]))