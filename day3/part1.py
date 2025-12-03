with open('input.txt') as f:
    lines = f.readlines()

total_joltage = 0

for pack in lines:
    first_digit = 9
    pack = pack.strip()
    while True:
        first_digit_str = str(first_digit)
        if first_digit_str not in pack:
           first_digit -= 1
           continue 
        index_highest_digit = pack.index(first_digit_str)
        if index_highest_digit+1 == len(pack):
            first_digit -= 1
            continue
        second_digit = max(int(d) for d in pack[index_highest_digit+1:])
        joltage = int(first_digit_str + str(second_digit))
        total_joltage += joltage
        break

print(total_joltage)
