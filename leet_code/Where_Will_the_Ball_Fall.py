class Solution:

    def findBall(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        ans = []
        for ball in range(cols):
            for row in grid:
                if (  # stuck
                        (ball == 0 and row[0] == -1)  # at left edge
                        or (ball == cols - 1 and row[-1] == 1)  # at right edge
                        or (row[ball] == 1 and row[ball + 1] == -1)  # "\/" on left
                        or (row[ball] == -1 and row[ball - 1] == 1)  # "\/" on right
                ):
                    ball = -1
                    break
                ball += row[ball]
            ans.append(ball)
        return ans


grid = [[1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1],
        [1, 1, 1, 1, 1, 1],
        [-1, -1, -1, -1, -1, -1]]
solve = Solution()
print(solve.findBall(grid))
