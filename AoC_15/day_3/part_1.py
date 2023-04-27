directions = []
with open("/Users/oliverjordan/AoC/2015/day_3/input_3.txt") as input:
    for line in input:
        for char in line:
            directions.append(char)

houses_visited = [[0,0]]
position = [0,0]
for dir in directions:
    if dir == '^':
        position[0] += 1
    elif dir == '<':
        position[1] -= 1
    elif dir == '>':
        position[1] += 1
    elif dir == 'v':
        position[0] -= 1
    
    has_been_visited = False
    for house in houses_visited:
        if house[0] == position[0] and house[1] == position[1]:
            has_been_visited = True
    if has_been_visited is False:
        houses_visited.append(position)

print(houses_visited)