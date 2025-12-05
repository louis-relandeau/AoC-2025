with open("input.txt") as f:
    lines = f.readlines()

ranges = []
for line in lines:
    if line.strip() == "":
        break
    ranges.append(tuple(sorted([int(id) for id in line.strip().split('-')])))
    assert ranges[-1][0] <= ranges[-1][1]

ranges.sort(key=lambda x: (x[0], x[1]))

total = 0
curr_min, curr_max = ranges[0]
for i in range(len(ranges)-1):
    if curr_max < ranges[i+1][0]:
        total += curr_max - curr_min + 1 
        curr_min, curr_max = ranges[i+1]
    else:
        curr_max = max(curr_max, ranges[i+1][1])
total += curr_max - curr_min + 1
print(total)