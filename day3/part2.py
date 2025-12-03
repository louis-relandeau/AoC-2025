with open('input.txt') as f:
    lines = f.readlines()

total_joltage = 0

for pack in lines:
    remaining_digits = 12
    all_digits = []
    pack = pack.strip()
    while remaining_digits:
        current_digit = 9
        while True:
            current_digit_str = str(current_digit)
            if current_digit_str not in pack:
                current_digit -= 1
                continue 
            index_highest_digit = pack.index(current_digit_str)
            if index_highest_digit+remaining_digits-1 >= len(pack):
                current_digit -= 1
                continue
            all_digits.append(current_digit_str)
            remaining_digits -= 1
            pack = pack[index_highest_digit+1:]
            break
    joltage = int(''.join(all_digits))
    total_joltage += joltage

print(total_joltage)
