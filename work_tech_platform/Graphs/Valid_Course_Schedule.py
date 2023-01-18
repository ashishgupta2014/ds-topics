"""
https://workat.tech/problem-solving/practice/valid-course-schedule

https://www.youtube.com/watch?v=WAOfKpxYHR8
"""
from collections import defaultdict
from typing import List


class Solution:

    def dfs(self, prerequisites, root, visited, path_visit):
        visited[root] = True
        path_visit[root] = True
        for node in prerequisites[root]:
            if not visited[node] and self.dfs(prerequisites, node, visited, path_visit):
                return True
            elif path_visit[node]:
                return True
        path_visit[root] = False
        return False

    def canCompleteProgram(self, n: int, prerequisites: List[List[int]]) -> bool:
        visited = [False]*n
        path_visit = [False]*n
        graph = defaultdict(list)
        for v, w in prerequisites:
            graph[w].append(v)
        for node in range(n):
            if not visited[node] and self.dfs(graph, node, visited, path_visit):
                return False
        return True

solve = Solution()
print(solve.canCompleteProgram(n=6, prerequisites=[[1, 0], [2, 0], [3, 1], [4, 3], [5, 4], [4, 2]]))



