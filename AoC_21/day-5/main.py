def join_points(x1, y1, x2, y2):
    result = []
    x_direction = 1 if x1 < x2 else -1
    y_direction = 1 if y1 < y2 else -1

    if x1 == x2:
        for j in range(y1, y2+y_direction, y_direction):
            result.append((x1, j))
        return result
    if y1 == y2:
        for i in range(x1, x2+x_direction, x_direction):
            result.append((i, y1))
        return result
    i, j = x1, y1
    while i != x2+x_direction and j!= y2+y_direction:
        result.append((i, j))
        i += x_direction
        j += y_direction
    return result

covered_points = []

with open('/Users/oliverjordan/AoC_21/day-5/input.txt') as input:
    for line in input:
        coords = list(map(lambda x: list(map(lambda y: int(y), x.split(','))),
                          line.rstrip('\n').split('->')))
        x1, y1 = coords[0]
        x2, y2 = coords[1]
        covered_points += join_points(x1, y1, x2, y2)

count = 0
for point in set(covered_points):
    if covered_points.count(point) > 1:
        count += 1
print(count)
