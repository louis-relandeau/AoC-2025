with open('day1/input.txt', 'r') as file:
    lines = file.readlines()

current_value = 50
zero_counter = 0

for line in lines:
    raw_thing = line.strip()
    direction = raw_thing[0]
    value = int(raw_thing[1:])

    zero_counter += value // 100
    value %= 100
    was_not_zero = current_value != 0
    
    if direction == 'L':
        current_value -= value
    elif direction == 'R':
        current_value += value

    if was_not_zero and (current_value <= 0 or current_value >= 100):
        zero_counter += 1
    
    current_value %= 100

print(zero_counter)