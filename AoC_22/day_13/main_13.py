import json
from functools import cmp_to_key

packets = []
with open('/Users/oliverjordan/AoC_22/day_13/input_13.txt') as input:
    for line in input:
        line = line.rstrip('\n')
        if line:
            listified_line = json.loads(line)
            packets.append(listified_line)

# -1 means keep same order, 1 means swap packets

def compare_ints(left, right):
    if left < right:
        return -1
    if right < left:
        return 1
    return None

def compare_list_and_int(left, right):
    if isinstance(left, int):
        return compare_lists([left], right)
    if isinstance(right, int):
        return compare_lists(left, [right])

def compare_lists(left, right):
    for i in range(len(left)):
        if i < len(right):
            if isinstance(left[i], list) and isinstance(right[i], list):
                if compare_lists(left[i], right[i]) is not None:
                    return compare_lists(left[i], right[i])
            elif isinstance(left[i], list) and isinstance(right[i], int) or \
            isinstance(left[i], int) and isinstance(right[i], list):
                if compare_list_and_int(left[i], right[i]) is not None:
                    return compare_list_and_int(left[i], right[i])
            else:
                if compare_ints(left[i], right[i]) is not None:
                    return compare_ints(left[i], right[i])
    if len(left) < len(right):
        return -1
    if len(right) < len(left):
        return 1
    return None

results = []
for i in range(0, len(packets), 2):
    results.append(compare_lists(packets[i], packets[i+1]))
total = 0
for i in range(len(results)):
    if results[i] == -1:
        total += i+1
print(total)

divider_1 = [[2]]
divider_2 = [[6]]
packets += [divider_1, divider_2]
sorted_packets = sorted(packets, key = cmp_to_key(compare_lists))
index_1 = sorted_packets.index(divider_1) + 1
index_2 = sorted_packets.index(divider_2) + 1
print(index_1*index_2)