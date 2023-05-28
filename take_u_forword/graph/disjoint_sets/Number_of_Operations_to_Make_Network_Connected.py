"""
https://leetcode.com/problems/number-of-operations-to-make-network-connected/

https://takeuforward.org/data-structure/number-of-operations-to-make-network-connected-dsu-g-49/

https://www.youtube.com/watch?v=FYrl7iz9_ZU
"""
from typing import List


class DisjointSet:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.parent = list(range(n))
        self.size = [1] * n

    def find_parent(self, node):
        if node == self.parent[node]:
            return node
        return self.find_parent(self.parent[node])

    def union_by_rank(self, u, v):
        parent_of_u = self.find_parent(u)
        parent_of_v = self.find_parent(v)
        if parent_of_v == parent_of_u:
            return
        elif self.rank[parent_of_u] < self.rank[parent_of_v]:
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

    def independent_nodes(self):
        count = 0
        for i, e in enumerate(self.parent):
            if i == e:
                count+= 1
        return count-1 if count > 0  else count

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        network = DisjointSet(n)
        extra_edges = 0
        for u, v in connections:
            if network.find_parent(u) == network.find_parent(v):
                extra_edges += 1
                continue
            network.union_by_size(u, v)
        node_count = network.independent_nodes()
        if node_count <= extra_edges:
            return node_count
        return -1

solve = Solution()
print(solve.makeConnected(n=4, connections=[[0,1],[0,2],[1,2]]))
print(solve.makeConnected(n=6, connections=[[0,1],[0,2],[0,3],[1,2]]))
print(solve.makeConnected(n=6, connections=[[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(solve.makeConnected(n=12, connections=[[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]))