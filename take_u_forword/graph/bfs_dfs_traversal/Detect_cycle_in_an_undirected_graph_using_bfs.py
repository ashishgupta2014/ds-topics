"""
https://takeuforward.org/data-structure/detect-cycle-in-an-undirected-graph-using-bfs/


"""
from typing import List


class Solution:

    def bfs(self, adjList, root, parent, visited):
        queue = [root]
        visited[root] = True
        while queue:
            node = queue.pop(0)
            for child in adjList[node]:
                if not visited[child]:
                    queue.append(child)
                    visited[child] = True
                    parent[child] = node
                elif parent[node] != child:
                    return True
        return False


    def isCycle(self, V, adjList: List[List[int]]) -> bool:
        visited = [False]*V
        parent = [-1]*V
        for node in range(V):
            if not visited[node] and self.bfs(adjList, node, parent, visited):
                return True
        return False

solve = Solution()
print(solve.isCycle(V=5, adjList=[[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]))
print(solve.isCycle(V=4, adjList=[[], [2], [1, 3], [2]]))