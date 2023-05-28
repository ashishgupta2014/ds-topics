"""
https://leetcode.com/problems/course-schedule-ii/

https://www.youtube.com/watch?v=WAOfKpxYHR8&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=25
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
        return result[::-1] if len(result) == self.V else []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = Graph(numCourses)
        for v, w in prerequisites:
            graph.addEdge(v, w)
        return graph.find_dependency()

solve = Solution()
print(solve.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(solve.findOrder(numCourses = 3, prerequisites = [[0,2],[1,2],[2,0]]))