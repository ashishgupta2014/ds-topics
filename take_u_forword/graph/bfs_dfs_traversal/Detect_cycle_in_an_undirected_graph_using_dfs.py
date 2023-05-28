"""
https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
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


    def isCycle(self, V, adjList: List[List[int]]) -> bool:
        visited = [False]*V
        for node in range(V):
            if not visited[node] and self.dfs(adjList, node, -1, visited):
                return True
        return False

solve = Solution()
print(solve.isCycle(V=5, adjList=[[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] ))