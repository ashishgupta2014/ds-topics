"""
https://practice.geeksforgeeks.org/problems/chocolates-pickup/1

https://takeuforward.org/data-structure/3-d-dp-ninja-and-his-friends-dp-13/

https://www.youtube.com/watch?v=QGfn7JeXK54
"""
class Solution:

    def dfs(self, grid, row, alice, bob, dp):
        if row >= len(grid) or alice >= len(grid[0]) or bob >= len(grid[0]):
            return -999999999
        if (row, alice, bob) in dp:
            return dp[(row, alice, bob)]
        if row == len(grid)-1:
            if alice == bob:
                return grid[row][alice]
            else:
                return grid[row][alice] + grid[row][bob]
        max_chocolate = float('-inf')
        for a in range(-1, 2):
            for b in range(-1, 2):
                if alice == bob:
                    ans = grid[row][alice] + self.dfs(grid, row+1, alice+a, bob+b, dp)
                else:
                    ans = grid[row][alice] + grid[row][bob] + self.dfs(grid, row + 1, alice + a, bob + b, dp)
                max_chocolate = max(max_chocolate, ans)
        dp[(row, alice, bob)] = max_chocolate
        return max_chocolate

    def solve(self, n, m, grid):
        dp = {}
        return self.dfs(grid, 0, 0, n-1, dp)

solve = Solution()
print(solve.solve(n=3, m=4, grid=[[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))