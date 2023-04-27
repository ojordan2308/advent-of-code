instructions = []
with open("/Users/oliverjordan/AoC_22/day_10/input_10.txt") as input:
    for line in input:
        line = line.rstrip('\n')
        instructions.append(line)

CYCLE = 1
X = 1
INCREMENT = 0
NICE = {}
NOT_NICE = {}

for instruction in instructions:
    if CYCLE in [21, 61, 101, 141, 181, 221]:
        NOT_NICE[CYCLE-1] = (CYCLE-1) * X
    X += INCREMENT
    if CYCLE in [20, 60, 100, 140, 180, 220]:
        NICE[CYCLE] = CYCLE * X
    if instruction == 'noop':
        CYCLE += 1
        INCREMENT = 0
    elif instruction[:4] == 'addx':
        CYCLE += 2
        INCREMENT = int(instruction[5:])

TOTAL = 0
for cycle in NICE:
    TOTAL += NICE[cycle]
for cycle in NOT_NICE:
    if cycle not in NICE:
        TOTAL += NOT_NICE[cycle]
print(TOTAL)