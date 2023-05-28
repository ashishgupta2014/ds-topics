"""
https://workat.tech/problem-solving/practice/minimum-spanning-tree-using-kruskals-algorithm

https://www.youtube.com/watch?v=aBxjDBC4M1U&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=46
https://www.youtube.com/watch?v=DMnDM_sxVig&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=47

"""
from typing import List

class Edge:
    def __init__(self, source: int, destination: int, weight=0):
        self.source = source
        self.destination = destination
        self.weight = weight



class Graph:
    def __init__(self, numVertices: int, edges: List[Edge]):
        self.numVertices = numVertices
        self.edges = edges


class DisjointSet:

    def __init__(self, numVertices):
        self.parent = {v: v for v in range(numVertices)}
        self.rank = {v: 0 for v in range(numVertices)}

    def find(self, vertex):
        if self.parent[vertex] == vertex:
            return vertex
        return self.find(self.parent[vertex])

    def union_by_rank(self, vertex_X, vertex_Y):
        parent_of_X = self.find(vertex_X)
        parent_of_Y = self.find(vertex_Y)
        if parent_of_X == parent_of_Y:
            return False
        if self.rank[parent_of_X] < self.rank[parent_of_Y]:
            self.parent[parent_of_X] = parent_of_Y
        elif self.rank[parent_of_X] > self.rank[parent_of_Y]:
            self.parent[parent_of_Y] = parent_of_X
        else:
            self.parent[parent_of_Y] = parent_of_X
            self.rank[parent_of_X] += 1
        return True

class Solution:
    def weightOfMST(self, graph: Graph) -> int:
        edges = sorted(graph.edges, key= lambda x: x.weight)
        ds = DisjointSet(graph.numVertices)
        min_sum = 0
        for edge in edges:
            if ds.union_by_rank(edge.source, edge.destination):
                min_sum += edge.weight
        return min_sum


solve = Solution()
g1 = Graph(numVertices=7, edges=[Edge(0, 1, 2),
                                    Edge(0, 3, 3),
                                    Edge(0, 6, 4),
                                    Edge(1, 2, 3),
                                    Edge(1, 4, 2),
                                    Edge(3, 4, 5),
                                    Edge(4, 5, 7),
                                    Edge(4, 6, 6)])

print(solve.weightOfMST(graph=g1))


