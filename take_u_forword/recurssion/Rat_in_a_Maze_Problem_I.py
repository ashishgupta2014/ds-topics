"""
https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

https://www.youtube.com/watch?v=bLGZhJlt4y0&list=PLgUwDviBIf0rGlzIn_7rsaR2FQ5e6ZOL9&index=18
"""

class Solution:
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    sign = ['D', 'R', 'L', 'U']

    def dfs(self, mat, row, col, path, result):
        if 0 > row or 0 > col or row >= len(mat) or col >= len(mat) or not mat[row][col]:
            return
        if row == len(mat)-1 and col == len(mat)-1 and mat[row][col]:
            result.append(''.join(path[:]))
            return
        for d, val in enumerate(self.directions):
            mat[row][col] = 0
            x, y = val
            path.append(self.sign[d])
            self.dfs(mat, row+x, col+y, path, result)
            path.pop()
            mat[row][col] = 1
    def findPath(self, m, n):
        result = []
        self.dfs(m, 0, 0, [], result)
        return result


if __name__ == '__main__':
    ob = Solution()
    n = 4
    matrix = [[1, 0, 0, 0],
              [1, 1, 0, 1],
              [1, 1, 0, 0],
              [0, 1, 1, 1]]
    result = ob.findPath(matrix, n)
    result.sort()
    if len(result) == 0:
        print(-1)
    else:
        for x in result:
            print(x, end=" ")
        print()