"""
https://workat.tech/problem-solving/practice/matrix-paths/editorial

https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
"""
class Solution:
    dp = [[0]*21 for _ in range(21)]
    def getNumPaths(self, rows: int, columns: int) -> int:
        if rows == 1 or columns == 1:
           return 1
        if self.dp[rows][columns] > 0:
            return self.dp[rows][columns]

        self.dp[rows][columns] = self.getNumPaths(rows-1, columns) + self.getNumPaths(rows, columns-1)
        return self.dp[rows][columns]

solve = Solution()
print(solve.getNumPaths(rows=2, columns=3))

print(solve.getNumPaths(rows=3, columns=3))

print(solve.getNumPaths(rows=5, columns=5))

print(solve.getNumPaths(rows=7, columns=5))