import os
# import download

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    res1 = 0
    res2 = 0
    for num in f.read().splitlines():
        max_num = 0
        for i in range(len(num) - 1):
            if int(num[i]) <= int(str(max_num)[0]):
                continue
            max_num = max(max_num, int(f"{num[i]}{max(num[i + 1:])}"))
        res1 += max_num
        batteries = 12
        num_len = len(num)
        last_index = 0
        max_num2 = ""
        while batteries != 0:
            curr_array = num[last_index:num_len-batteries+1]
            curr_index = curr_array.find(max(curr_array))
            last_index += 1+curr_index
            max_num2 += curr_array[curr_index]
            batteries -= 1
        res2 += int(max_num2)

print(res1)
print(res2)
