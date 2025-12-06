with open('input.txt') as f:
    rows = [r.replace('\n','') for r in f.readlines()]

current_numbers = []
total = 0
for i in reversed(range(len(rows[0]))):
    number = ''.join([rows[j][i] for j in range(len(rows)-1)])
    if not number.strip():
        continue
    current_numbers.append(int(number))

    op = rows[-1][i]
    if op.strip():
        if op == '+':
            total += sum(current_numbers)
        else:
            sub_total = 1
            for n in current_numbers:
                sub_total *= n
            total += sub_total
        current_numbers.clear()

print(total)