import os
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    original_lines = f.read().split("\n")
    lines = [line.split() for line in original_lines]
    for line in zip(*lines):
        res1 += eval(line[-1].join(line[:-1]))

    temp = ""
    for i in range(len(original_lines[0])-1, -1, -1):
        for j in range(len(original_lines)):
            temp += original_lines[j][i]
        if temp[-1] in ["*", "+"]:
            res2 += eval(temp[-1].join(temp[:-1].split()))
            temp = ""
print(res1)
print(res2)
