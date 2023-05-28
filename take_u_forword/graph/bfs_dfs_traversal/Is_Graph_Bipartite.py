"""
https://leetcode.com/problems/is-graph-bipartite/description/

https://takeuforward.org/graph/bipartite-graph-dfs-implementation/
"""
from typing import List


class Solution:

    def bfs(self, root, graph, color):
        queue = [root]
        color[root] = 0
        while queue:
            node = queue.pop(0)
            connected_nodes = graph[node]
            for n in connected_nodes:
                if color[n] == color[node]:
                    return False
                if color[n] == -1:
                    if color[node] == 0:
                        color[n] = 1
                    else:
                        color[n] = 0
                    queue.append(n)
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        for node in range(len(graph)):
            if color[node] == -1 and self.bfs(node, graph, color) is False:
                return False
        return True

solve = Solution()
print(solve.isBipartite(graph=[[1,2,3],[0,2],[0,1,3],[0,2]]))
print(solve.isBipartite(graph=[[1,3],[0,2],[1,3],[0,2]]))
print(solve.isBipartite(graph=[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))

class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for node_from in range(len(graph)):
            if node_from not in colors and not self.dfs(graph, node_from, colors, 1):
                return False

        return True

    def dfs(self, graph, node, colors, color):

        colors[node] = color

        for node_to in graph[node]:
            if node_to in colors:
                if colors[node_to] == colors[node]:
                    return False
            else:
                if not self.dfs(graph, node_to, colors, color * -1):
                    return False

        return True
solve = Solution2()
print(solve.isBipartite(graph=[[1,2,3],[0,2],[0,1,3],[0,2]]))
print(solve.isBipartite(graph=[[1,3],[0,2],[1,3],[0,2]]))
print(solve.isBipartite(graph=[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]))