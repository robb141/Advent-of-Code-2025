import os
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    dial = 50
    for line in f.read().splitlines():
        direction, distance = line[0], int(line[1:])
        if direction == "L":
            if dial == 0:
                res2 -= 1
            new_dial = (dial - distance)
            dial = new_dial % 100
            if new_dial <= 0:
                res2 += (new_dial // -100) + 1
        elif direction == "R":
            new_dial = (dial + distance)
            dial = new_dial % 100
            res2 += new_dial // 100
        else:
            raise "Not a valid direction"
        if dial == 0:
            res1 += 1
print(res1)
print(res2)
