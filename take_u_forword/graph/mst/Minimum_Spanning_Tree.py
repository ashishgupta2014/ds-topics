"""
https://takeuforward.org/data-structure/prims-algorithm-minimum-spanning-tree-c-and-java-g-45/
"""
import heapq
from collections import defaultdict


class Solution:

    def spanningTree(self, V, adj):
        graph = defaultdict(list)
        for u, v, w in adj:
            graph[u].append((w, v))
            graph[v].append((w, u))

        queue = [(0, 0)]
        heapq.heapify(queue)

        min_sum = 0
        visited = [False] * V

        while queue:
            wt, node = heapq.heappop(queue)
            if visited[node]:
                continue
            visited[node] = True
            min_sum += wt
            for w, n in graph[node]:
                if not visited[n]:
                    heapq.heappush(queue, (w, n))
        return min_sum


solve = Solution()
print(solve.spanningTree(V=5, adj=[[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [4, 2, 7]]))