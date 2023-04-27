from part_1 import priority

bags = []

with open('/Users/oliverjordan/AoC_22/day_3/input_3.txt') as input:
    for line in input:
        contents = line. rstrip('\n')
        bags.append(contents)

groups = []
for i in range(0, len(bags), 3):
    group = [bags[i], bags[i+1], bags[i+2]]
    groups.append(group)

def find_badge(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return item
        
badges = list(map(find_badge, groups))

badge_priorities = list(map(lambda x: priority.index(x) + 1,  badges))

print(sum(badge_priorities))