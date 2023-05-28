"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
https://takeuforward.org/data-structure/most-stones-removed-with-same-row-or-column-dsu-g-53/
https://www.youtube.com/watch?v=OwMNX8SPavM
"""
from typing import List

class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)

    def find_parent(self, node):
        if node == self.parent[node]:
            return node
        return self.find_parent(self.parent[node])

    def union_by_rank(self, u, v):
        parent_of_u = self.find_parent(u)
        parent_of_v = self.find_parent(v)
        if self.rank[parent_of_u] < self.rank[parent_of_v]:
            self.parent[parent_of_u] = parent_of_v
        elif self.rank[parent_of_u] > self.rank[parent_of_v]:
            self.parent[parent_of_v] = parent_of_u
        else:
            self.parent[parent_of_v] = parent_of_u
            self.rank[parent_of_u] += 1

    def union_by_size(self, u, v):
        parent_of_u = self.find_parent(u)
        parent_of_v = self.find_parent(v)
        if parent_of_v == parent_of_u:
            return
        elif self.size[parent_of_u] < self.size[parent_of_v]:
            self.parent[parent_of_u] = parent_of_v
            self.size[parent_of_v] += self.size[parent_of_u]
        else:
            self.parent[parent_of_v] = parent_of_u
            self.size[parent_of_u] += self.size[parent_of_v]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_row = max_col = 0
        for r, c in stones:
            max_row = max(max_row, r)
            max_col = max(max_col, c)
        ds = DisjointSet(n=max_row+max_col+1)
        stoneNodes = {}
        for r, c in stones:
            col = c + max_row + 1
            ds.union_by_size(r, col)
            stoneNodes[r] = 1
            stoneNodes[col] = 1
        count = 0
        for key, _ in stoneNodes.items():
            if ds.find_parent(key) == key:
                count += 1
        return len(stones) - count


solve = Solution()
print(solve.removeStones(stones=[[0,0],[0,2],[1,1],[2,0],[2,2]]))