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
        for j in range(1, digit_length):
            if digit_length % j != 0:
                continue
            sub_strings = [str(i)[k:k+j] for k in range(0, digit_length, j)]
            if all(s == sub_strings[0] for s in sub_strings):
                total += i
                break

print(total)