"""
https://workat.tech/problem-solving/practice/detect-cycle-in-undirected-graph

https://www.youtube.com/watch?v=Y9NFqI6Pzd4
"""
from typing import List


class Solution:

    def dfs(self, adjList, root, parent, visited):
        visited[root] = True
        for node in adjList[root]:
            if node != parent and visited[node]:
                return True
            elif node != parent and self.dfs(adjList, node, root, visited):
                return True
        return False


    def isCyclic(self, adjList: List[List[int]]) -> bool:
        visited = [False]*len(adjList)
        for node in range(len(adjList)):
            if not visited[node] and self.dfs(adjList, node, -1, visited):
                return True
        return False

solve = Solution()

print(solve.isCyclic(adjList=[[0, 1], [0, 2], [2, 3], [2, 4], [3, 4]]))



