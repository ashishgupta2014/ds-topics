"""
https://leetcode.com/problems/number-of-provinces/description/

https://practice.geeksforgeeks.org/problems/number-of-provinces/1

https://www.youtube.com/watch?v=ACzkVtewUYA
"""
from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list = defaultdict(list)
        for row in range(n):
            for col in range(row + 1, n):
                if isConnected[row][col] == 1:
                    adj_list[row + 1].append(col + 1)
                    adj_list[col + 1].append(row + 1)

        def dfs(city):
            if city in visited:
                return False
            visited.add(city)
            neighbours = adj_list[city]
            for padosi in neighbours:
                dfs(padosi)
            return True

        visited = set()
        provinces = 0
        for city in range(1, n + 1):
            if city not in visited and dfs(city):
                provinces += 1
        return provinces

solve = Solution()
print(solve.findCircleNum(isConnected=[[1,1,0],[1,1,0],[0,0,1]]))
print(solve.findCircleNum(isConnected=[[1,0,0],[0,1,0],[0,0,1]]))
print(solve.findCircleNum(isConnected=[[1,1,1],[1,1,1],[1,1,1]]))