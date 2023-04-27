# part 1
x = 0
y = 0

with open('/Users/oliverjordan/AoC_21/day-2/input.txt') as input:
    for line in input:
        instruction = line.rstrip('\n')
        [direction, amount] = instruction.split(' ')
        if direction == 'forward':
            x += int(amount)
        elif direction == 'up':
            y -= int(amount)
        elif direction == 'down':
            y += int(amount)

print(x*y)

# part 2
x = 0
y = 0
aim = 0

with open('/Users/oliverjordan/AoC_21/day-2/input.txt') as input:
    for line in input:
        instruction = line.rstrip('\n')
        [direction, amount] = instruction.split(' ')
        if direction == 'forward':
            x += int(amount)
            y += (aim * int(amount))
        elif direction == 'up':
            aim -= int(amount)
        elif direction == 'down':
            aim += int(amount)

print(x*y)