def floodFill(image, sr, sc, color):
    queue = [(sr, sc)]
    filled = image[sr][sc]
    if filled == color:
        return image
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(image)
    cols = len(image[0])
    while queue:
        row, col = queue.pop(0)
        image[row][col] = color
        for r, c in direction:
            c_r = row + r
            c_c = col + c
            if 0 <= c_r < rows and 0 <= c_c < cols and image[c_r][c_c] == filled:
                queue.append((c_r, c_c))


image = [[0, 0, 0],
         [0, 1, 0]]
sr = 1
sc = 1
color = 2
floodFill(image, sr, sc, color)
print(image)
