with open("input.txt") as f:
    lines = f.readlines()

fresh_ranges = []
available = []
in_ranges = True
for line in lines:
    if line.strip() == "":
        in_ranges = False
    elif in_ranges:
        fresh_ranges.append(tuple([int(id) for id in line.strip().split('-')]))
    else:
        available.append(int(line.strip()))

fresh_count = 0
for a in available:
    for r in fresh_ranges:
        if a >= r[0] and a <= r[1]:
            fresh_count += 1
            break

print(fresh_count)