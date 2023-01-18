"""
https://workat.tech/problem-solving/practice/m-coloring-problem
https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1

https://www.youtube.com/watch?v=wuVwUK25Rfc
"""
from typing import List


class Solution:
    adjMatrix = []

    def is_possible(self, n, c, colors):
        for node in self.adjMatrix[n]:
            if colors[node] == c:
                return False
        return True

    def dfs(self, n, m, colors):
        if n == len(self.adjMatrix):
            return True
        for c in range(m):
            if self.is_possible(n, c, colors):
                colors[n] = c
                if self.dfs(n+1, m, colors):
                    return True
                colors[n] = None
        return False
    def isColoringPossible(self, adjMatrix: List[List[int]], m: int) -> bool:
        self.adjMatrix = adjMatrix
        nodes = len(adjMatrix)
        colors = [None]*nodes
        return self.dfs(0, m, colors)


solve = Solution()
print(solve.isColoringPossible(adjMatrix=[[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]], m=3))
print(solve.isColoringPossible(adjMatrix=[[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]], m=2))



