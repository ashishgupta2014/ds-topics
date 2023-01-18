"""
https://workat.tech/problem-solving/practice/shortest-paths-using-dijkstras-algorithm

https://www.youtube.com/watch?v=V6H1qAeB-l4&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=32
"""
import heapq
from typing import List

class Edge:
    def __init__(self, source: int, destination: int, cost=0):
        self.source = source
        self.destination = destination
        self.cost = cost

class Graph:
    def __init__(self, numVertices: int, edges: List[Edge]):
        self.numVertices = numVertices
        self.edges = edges

class PathNode:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
class Solution:
    def getMinCosts(self, graph: Graph) -> List[int]:
        adj_list = {}
        for edge in graph.edges:
            if edge.source in adj_list:
                adj_list[edge.source].append(PathNode(node=edge.destination, cost=edge.cost))
            else:
                adj_list[edge.source] = [PathNode(node=edge.destination, cost=edge.cost)]

            if edge.destination in adj_list:
                adj_list[edge.destination].append(PathNode(node=edge.source, cost=edge.cost))
            else:
                adj_list[edge.destination] = [PathNode(node=edge.source, cost=edge.cost)]
        queue = [PathNode(node=0, cost=0)]
        heapq.heapify(queue)
        path_cost = [float('inf')]*graph.numVertices
        path_cost[0] = 0
        while queue:
            node = heapq.heappop(queue)
            connected_nodes = adj_list[node.node]
            for n in connected_nodes:
                cost = path_cost[node.node] + n.cost
                if cost < path_cost[n.node]:
                    path_cost[n.node] = cost
                    heapq.heappush(queue, PathNode(node=n.node, cost=cost))
        return path_cost



solve = Solution()
g1 = Graph(numVertices=7, edges=[Edge(0, 1, 2),
                                 Edge(0, 3, 3),
                                 Edge(0, 6, 4),
                                 Edge(1, 2, 3),
                                 Edge(1, 4, 2),
                                 Edge(3, 4, 5),
                                 Edge(4, 5, 7),
                                 Edge(4, 6, 6)])

print(solve.getMinCosts(graph=g1))




