"""
https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1

https://www.youtube.com/watch?v=YbY8cVwWAvw&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=42

https://takeuforward.org/data-structure/floyd-warshall-algorithm-g-42/
"""
class Solution:
	def shortest_distance(self, matrix):
		n = len(matrix)
		for i in range(n):
			for j in range(n):
				if matrix[i][j] == -1:
					matrix[i][j] = 1e9
				if i == j:
					matrix[i][j] = 0
		for k in range(n):
			for i in range(n):
				for j in range(n):
					matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
		for i in range(n):
			for j in range(n):
				if matrix[i][j] == 1e9:
					matrix[i][j] = -1
		return matrix

solve = Solution()
print(solve.shortest_distance(matrix = [[0,1,43],[1,0,6],[-1,-1,0]]))