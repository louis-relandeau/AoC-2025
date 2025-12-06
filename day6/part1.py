with open('input.txt') as f:
    lines = f.readlines()

rows = [[c.strip() for c in v.split(' ') if c.strip()] for v in lines]

total = 0
for i in range(len(rows[0])):
    if rows[-1][i] == '+':
        sub_total = 0
        for j in range(len(rows)-1):
            sub_total += int(rows[j][i])
    else:
        sub_total = 1
        for j in range(len(rows)-1):
            sub_total *= int(rows[j][i])
    total += sub_total
print(total)