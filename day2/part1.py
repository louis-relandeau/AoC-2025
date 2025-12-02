with open("input.txt") as f:
    line = f.readline().strip()

total = 0

ranges = line.split(",")
for r in ranges:
    split_range = r.split("-")
    start = int(split_range[0])
    end = int(split_range[1])
    
    for i in range(start, end + 1):
        digit_length = len(str(i))
        if digit_length % 2 != 0:
            continue
        first_half = str(i)[:digit_length // 2]
        second_half = str(i)[digit_length // 2:]
        if first_half == second_half:
            total += i

print(total)