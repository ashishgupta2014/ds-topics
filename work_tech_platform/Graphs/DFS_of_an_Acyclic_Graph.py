"""
https://workat.tech/problem-solving/practice/dfs-of-acyclic-graph

https://workat.tech/problem-solving/approach/doag/dfs-of-acyclic-graph
"""

from typing import List


class Solution:

    def preorder(self, adj, parent, root, result):
        result.append(root)
        for node in adj[root]:
            if node != parent:
                self.preorder(adj, root, node, result)
    def dfs(self, adjList: List[List[int]]) -> List[int]:
        result = []
        self.preorder(adjList, -1, 0, result)
        return result

solve = Solution()

print(solve.dfs(adjList=[[1, 3, 6], [0, 2, 4], [1], [0], [1, 5], [4], [0]]))





