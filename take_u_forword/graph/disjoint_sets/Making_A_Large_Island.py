"""
https://leetcode.com/problems/making-a-large-island/description/

https://takeuforward.org/data-structure/making-a-large-island-dsu-g-52/


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
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        ds = DisjointSet(rows*cols)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    for x, y in directions:
                        r = row+x
                        c = col+y
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c]:
                            node_no = row*cols+col
                            adj_node_no = r*cols+c
                            ds.union_by_size(node_no, adj_node_no)

        max_size = 0
        for row in range(rows):
            for col in range(cols):
                if not grid[row][col]:
                    components = set()
                    for x, y in directions:
                        r = row+x
                        c = col+y
                        if 0 <= r < rows and 0 <= c < cols and grid[r][c]:
                            components.add(ds.find_parent(r*cols+c))
                    total_size = 1
                    for n in components:
                        total_size += ds.size[n]
                    max_size = max(max_size, total_size)
        if max_size == 0:
            return sum([grid[i][j] for j in range(cols) for i in range(rows)])
        return max_size

solve = Solution()
print(solve.largestIsland(grid=[[1,0],[0,1]]))
print(solve.largestIsland(grid=[[0,0],[0,0]]))
print(solve.largestIsland(grid=[[0,0],[0,1]]))
print(solve.largestIsland(grid=[[1,1],[1,1]]))
print(solve.largestIsland(grid=[[1,1],[1,0]]))