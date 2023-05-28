"""
https://leetcode.com/problems/find-eventual-safe-states/description/

https://www.youtube.com/watch?v=2gtg3VsDGyc&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=26
"""
from collections import defaultdict
from typing import List

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)

    def find_dependency(self):
        in_order = [0]*self.V
        for v in range(self.V):
            for x in self.graph[v]:
                in_order[x] += 1
        queue = [i for i, x in enumerate(in_order) if x == 0]

        result = []
        while queue:
            node = queue.pop(0)
            result.append(node)
            for v in self.graph[node]:
                in_order[v] -= 1
                if in_order[v] == 0:
                    queue.append(v)
        return result

class Solution:
    def eventualSafeNodes(self, arr: List[List[int]]) -> List[int]:
        graph = Graph(len(arr))
        for u, v in enumerate(arr):
            for e in v:
                graph.addEdge(e, u)
        return sorted(graph.find_dependency())

solve = Solution()
print(solve.eventualSafeNodes(arr=[[1,2],[2,3],[5],[0],[5],[],[]]))