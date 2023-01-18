from typing import List


class Solution:
    def adjListToMatrix(self, n: int, adjList: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for _ in range(n)]

        for node, path in enumerate(adjList):
            for p in path:
                mat[node][p] = 1
        return mat


solve = Solution()
print(solve.adjListToMatrix(n=4, adjList=[[1, 2, 3], [0], [0, 3], [0, 2]]))



