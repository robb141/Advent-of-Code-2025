import os
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    ranges = []
    nums = []
    for line in f.read().splitlines():
        if "-" in line:
            ranges.append([int(x) for x in line.split("-")])
        elif line != "":
            nums.append(int(line))
    for num in nums:
        in_range = False
        for r in ranges:
            low, high = r
            if low <= num <= high:
                in_range = True
        if in_range:
            res1 += 1
    changes = True

    while changes:
        fresh_len = len(ranges)
        new = [ranges[0]]
        for r in ranges[1:]:
            low, high = r
            ignore = False
            for n in range(len(new)):
                low_new, high_new = new[n]
                if low <= low_new <= high_new <= high:
                    # overlap whole
                    # [1, 4] [2, 3]-new
                    new[n] = [min(low, low_new), max(high, high_new)]
                    ignore = True
                    break
                elif low_new <= low <= high <= high_new:
                    # overlap whole
                    # [2, 3] [1, 4]-new
                    ignore = True
                    break
                elif low <= low_new <= high <= high_new:
                    # overlap high
                    # [1, 4] [3, 6]-new
                    new[n] = [min(low, low_new), max(high, high_new)]
                    ignore = True
                    break
                elif low_new <= low <= high_new <= high:
                    # overlap low
                    # [3, 6] [1, 4]-new
                    # [12, 18] [16, 20]-new
                    new[n] = [min(low, low_new), max(high, high_new)]
                    ignore = True
                    break
            if not ignore:
                new.append(r)
        ranges = new
        if fresh_len == len(ranges):
            changes = False
            break
    for n in new:
        res2 += (n[1] - n[0] + 1)

print(res1)
print(res2)
