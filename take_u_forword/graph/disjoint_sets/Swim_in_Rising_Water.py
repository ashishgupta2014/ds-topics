"""
https://leetcode.com/problems/swim-in-rising-water/description/


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
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cells = [(grid[i][j], i, j) for j in range(n) for i in range(n)]
        cells.sort()
        ds = DisjointSet(n*n)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for elevation, row, col in cells:
            cell = row*n+col
            for x, y in directions:
                r = row+x
                c = col+y
                if 0 <= r < n and 0 <= c < n and grid[r][c] <= elevation:
                    adj_cell = r*n+c
                    ds.union_by_size(cell, adj_cell)
            if ds.find_parent(0) == ds.find_parent(n*n-1):
                return elevation
        return -1

solve = Solution()
print(solve.swimInWater(grid=[[0,2],[1,3]]))