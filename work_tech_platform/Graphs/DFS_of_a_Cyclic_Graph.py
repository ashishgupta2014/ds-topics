"""
https://workat.tech/problem-solving/practice/dfs-of-cyclic-graph

https://workat.tech/problem-solving/approach/docg/dfs-of-cyclic-graph


"""
from typing import List


class Solution:
    is_visited = {}

    def preorder(self, adj, root, result):
        result.append(root)
        self.is_visited[root] = True
        for node in adj[root]:
            if self.is_visited[node] is False:
                self.preorder(adj, node, result)
    def dfs(self, adjList: List[List[int]]) -> List[int]:
        result = []
        self.is_visited = {i: False for i in range(len(adjList))}
        self.preorder(adjList, 0, result)
        return result

solve = Solution()
print(solve.dfs(adjList=[[1, 2, 3], [0], [0, 3], [0, 2]]))