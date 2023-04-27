rucksacks = []

with open('/Users/oliverjordan/AoC_22/day_3/input_3.txt') as input:
    for line in input:
        contents = line.rstrip('\n')
        l = len(contents)
        rucksacks.append([contents[:l//2], contents[l//2:]])

def find_common_item(bag):
    for item in bag[0]:
        if item in bag[1]:
            return item

common_items = list(map(find_common_item, rucksacks))

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
item_priorities = list(map(lambda x: priority.index(x) + 1,  common_items))
print(sum(item_priorities))