import os
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    grid = f.read().splitlines()
    R = len(grid)
    C = len(grid[0])
    run = 0
    while True:
        to_remove = []
        for r in range(R):
            for c in range(C):
                rolls = 0
                if grid[r][c] == "@":
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            else:
                                if 0 <= r+dx < R and 0 <= c+dy < C and grid[r+dx][c+dy] == "@":
                                    rolls += 1
                    if rolls < 4:
                        to_remove.append([r, c])
        if not to_remove:
            break
        if run == 0:
            res1 = len(to_remove)
        res2 += len(to_remove)
        run += 1
        for elem in to_remove:
            grid[elem[0]] = grid[elem[0]][:elem[1]] + "." + grid[elem[0]][elem[1] + 1:]
print(res1)
print(res2)
