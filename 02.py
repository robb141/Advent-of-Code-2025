import os
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    for line in f.readlines():
        for rng in line.split(","):
            first, second = [int(x) for x in rng.split("-")]
            for num in range(first, second+1):
                num_str, num_length = str(num), len(str(num))
                if num_length % 2 == 0 and num_str[0: num_length//2] == num_str[num_length//2:]:
                    res1 += num
                for i in range(1, num_length//2+1):
                    if num_str[0:i]*(num_length//i) == num_str:
                        res2 += num
                        break
print(res1)
print(res2)
