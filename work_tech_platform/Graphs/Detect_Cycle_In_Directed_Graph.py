"""
https://workat.tech/problem-solving/practice/detect-cycle-in-directed-graph

https://www.youtube.com/watch?v=9twcmtQj4DU
"""

from typing import List


class Solution:
    visited = []
    def dfs(self, adList, root, path_visited):
        self.visited[root] = True
        path_visited[root] = True
        for node in adList[root]:
            if not self.visited[node]:
                if self.dfs(adList, node, path_visited):
                    return True
            elif path_visited[node]:
                return True
        path_visited[root] = False
        return False

    def isCyclic(self, adjList: List[List[int]]) -> bool:
        self.visited = [False]*len(adjList)
        path_visited = [False]*len(adjList)
        for node in range(len(adjList)):
            if not self.visited[node] and self.dfs(adjList, node, path_visited):
                return True
        return False


solve = Solution()
print(solve.isCyclic(adjList=[[1], [2], [0]]))
print(solve.isCyclic(adjList=[[1, 3, 6], [2, 4], [], [], [5], [], []]))

print(solve.isCyclic(adjList=[[1], [2], [3, 6], [4], [5], [], [4]]))

print(solve.isCyclic(adjList=[[1], [2], [3, 6], [4], [5], [], [4], [1, 8], [9], [7]]))