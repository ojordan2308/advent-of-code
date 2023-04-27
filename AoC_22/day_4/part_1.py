pairs = []
with open('/Users/oliverjordan/AoC_22/day_4/input_4.txt') as input:
    for line in input:
        sections = line.rstrip('\n').replace(',','-').split('-')
        num_sections = list(map(lambda x: int(x), sections))
        pairs.append(num_sections)

def completely_contain(list):
    if list[0] >= list[2] and list[1] <= list[3]:
        return True
    if list[2] >= list[0] and list[3] <= list[1]:
        return True
    return False

overlapping_pairs = list(filter(completely_contain, pairs))
print(len(overlapping_pairs))
