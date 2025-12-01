with open('day1/input.txt', 'r') as file:
    lines = file.readlines()

current_value = 50
zero_counter = 0

for line in lines:
    raw_thing = line.strip()
    direction = raw_thing[0]
    value = int(raw_thing[1:])
    
    if direction == 'L':
        current_value -= value
    elif direction == 'R':
        current_value += value
    
    current_value %= 100
    if current_value == 0:
        zero_counter += 1

print(zero_counter)