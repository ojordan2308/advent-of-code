calories_by_elf = []
with open('/Users/oliverjordan/AoC_22/day_1/input_1.txt', 'r') as input:
    elf = []
    for line in input:
        if line == '\n':
            calories_by_elf.append(elf)
            elf = []
        else:
            elf.append(int(line))

caloric_totals = []
for elf in calories_by_elf:
    caloric_totals.append(sum(elf))

max = max(caloric_totals)
print(max)
sorted_list = sorted(caloric_totals)
big_three = sorted_list[-3:]
print(sum(big_three))
