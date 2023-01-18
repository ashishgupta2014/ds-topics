"""
https://workat.tech/problem-solving/practice/path-exists-in-directed-graph

https://www.codingninjas.com/codestudio/problem-details/path-between-two-vertices-in-a-directed-graph_920534

https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/
"""
from typing import List


class Solution:

    def dfs(self, adjList, root, visited):
        visited[root] = True
        for node in adjList[root]:
            if not visited[node]:
                self.dfs(adjList, node, visited)
    def pathExists(self, adjList: List[List[int]]) -> bool:
        visited = [False]*len(adjList)
        self.dfs(adjList, 0, visited)
        return True if visited[-1] else False

solve = Solution()
print(solve.pathExists(adjList=[[1], [2, 0], [0, 3], [1]]))

print(solve.pathExists(adjList=[[1], [0], [0, 1, 3], [1]]))
