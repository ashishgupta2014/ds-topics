"""
https://workat.tech/problem-solving/practice/minimum-spanning-tree-using-prims-algorithm

https://www.youtube.com/watch?v=mJcZjjKzeqk&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=45
"""
import heapq
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

class VertexDirections:
    def __init__(self, parent, node, weight):
        self.parent = parent
        self.node = node
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight
class Solution:
    def weightOfMST(self, graph: Graph) -> int:
        matrix = [[0]*graph.numVertices for _ in range(graph.numVertices)]
        for edge in graph.edges:
            matrix[edge.source][edge.destination] = edge.weight
            matrix[edge.destination][edge.source] = edge.weight
        queue = [VertexDirections(parent=-1, node=0, weight=0)]
        heapq.heapify(queue)
        visited = [False]*graph.numVertices
        min_sum = 0
        while queue:
            edge = heapq.heappop(queue)
            if not visited[edge.node]:
                min_sum += edge.weight
                visited[edge.node] = True
                nodes = matrix[edge.node]
                for node, wt in enumerate(nodes):
                    if not visited[node] and wt > 0:
                        heapq.heappush(queue, VertexDirections(parent=edge.node, node=node, weight=wt))
        return min_sum



if __name__ == '__main__':
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

    g2 = Graph(numVertices=3, edges=[Edge(0, 1, 5), Edge(0, 2, 1), Edge(1, 2, 3)])
    print(solve.weightOfMST(graph=g2))