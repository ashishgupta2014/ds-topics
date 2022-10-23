direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                count += 1
                bfs(grid, row, col, rows, cols)
    return count


def bfs(grid, row, col, rows, cols):
    queue = [(row, col)]
    while queue:
        row, col = queue.pop(0)
        grid[row][col] = '@'
        for r, c in direction:
            c_r = row + r
            c_c = col + c
            if 0 <= c_r < rows and 0 <= c_c < cols and grid[c_r][c_c] == '1':
                queue.append((c_r, c_c))


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["1", "0", "0", "0", "0"]
]

print(numIslands(grid))
print(grid)
