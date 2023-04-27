stacks = {1: ['G', 'D', 'V', 'Z', 'J', 'S', 'B'],
          2: ['Z', 'S', 'M', 'G', 'V', 'P'],
          3: ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],
          4: ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
          5: ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
          6: ['R', 'G', 'C', 'D'],
          7: ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
          8: ['P', 'F', 'V'],
          9: ['D', 'R', 'S', 'T', 'J']}

instructions = []
with open('/Users/oliverjordan/AoC_22/day_5/input_5.txt') as input:
    for line in input:
        instruction = []
        words = line.rstrip('\n').split(' ')
        for word in words:
            if word.isdigit():
                instruction.append(int(word))
        instructions.append(instruction)


def move_stacks(num_crates, init_stack, target_stack):
    count = 0
    while count < num_crates:
        if len(stacks[init_stack]) > 0:
            crate = stacks[init_stack].pop()
            stacks[target_stack].append(crate)
        count += 1
    return

for i in instructions:
    move_stacks(i[0], i[1], i[2])

result = ''
for stack in stacks:
    result += stacks[stack][-1]

print(result)