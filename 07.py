import os
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    grid = f.read().splitlines()
    R = len(grid)
    C = len(grid[0])
    beams = [[0, grid[0].find('S')]]
    dotted_line = grid[1]
    timelines = [1 if grid[0][i] == "S" else 0 for i in range(len(grid[0]))]
    for r in range(1, R):
        beams = [[x + 1, y] for x, y in beams]
        if grid[r] == dotted_line:
            continue
        for c in range(C):
            if grid[r][c] == "^" and [r, c] in beams:
                beams.remove([r, c])
                res1 += 1
                if [r, c-1] not in beams and grid[r][c-1] != "^":
                    beams.append([r, c-1])
                if [r, c+1] not in beams and grid[r][c+1] != "^":
                    beams.append([r, c+1])
                timelines[c-1] += timelines[c]
                timelines[c+1] += timelines[c]
                timelines[c] = 0
print(res1)
print(sum(timelines))
