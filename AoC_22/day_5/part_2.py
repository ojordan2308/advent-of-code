from part_1 import instructions

stacks = {1: ['G', 'D', 'V', 'Z', 'J', 'S', 'B'],
          2: ['Z', 'S', 'M', 'G', 'V', 'P'],
          3: ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],
          4: ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
          5: ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
          6: ['R', 'G', 'C', 'D'],
          7: ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
          8: ['P', 'F', 'V'],
          9: ['D', 'R', 'S', 'T', 'J']}

def move_stacks(num_crates, init_stack, target_stack):
    crates = stacks[init_stack][-num_crates:]
    stacks[target_stack] += crates
    stacks[init_stack] = stacks[init_stack][:-num_crates]

for i in instructions:
    move_stacks(i[0], i[1], i[2])

result = ''
for stack in stacks:
    result += stacks[stack][-1]

print(result)