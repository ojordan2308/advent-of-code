rocks_corners = []
with open('/Users/oliverjordan/AoC_22/day_14/input_14.txt') as input:
    for line in input:
        line = line.rstrip('\n')
        coords = list(map(lambda x: list(map(lambda y: int(y), x.strip().split(','))),
                        line.split('->')))
        rocks_corners.append(coords)

max_x = 0
min_x = 1000
max_y = 0
min_y = 1000
for thing in rocks_corners:
    for point in thing:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
        if point[0] < min_x:
            min_x = point[0]
        if point[1] < min_y:
            min_y = point[1]


def join_corners(left, right):
    [lx, ly] = left
    [rx, ry] = right
    edges = []
    direction = 1 if (lx < rx or ly < ry) else -1
    for i in range(lx, rx, direction):
        edges.append([i, ly])
    for j in range(ly, ry, direction):
        edges.append([lx, j])
    edges.append(right)
    return edges

rocks_edges = []
for rock in rocks_corners:
    for i in range(1, len(rock)):
        rocks_edges += join_corners(rock[i-1], rock[i])

grid = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append('.')
    grid.append(row)

for point in rocks_edges:
    x = point[0]
    y = point[1]
    grid[y][x] = '#'

def display_gid(x1, x2, y1, y2):
    for row in grid[y1: y2+1]:
        print(''.join(row[x1: x2+1]))

grid_window = [min_x-3, max_x+3, 0, max_y+3]
#display_gid(*grid_window)

def drop_sand(x, y):
    is_moving = True
    j = y
    i = x
    while is_moving:
        if grid[j+1][i] == '.':
            j += 1
        elif grid[j+1][i-1] == '.':
            i -= 1
        elif grid[j+1][i+1] == '.':
            i += 1
        else:
            is_moving = False
    grid[j][i] = 'o'
    #display_gid(*grid_window)

def reset_grid():
    for row in grid:
        for point in row:
            if point == 'o':
                point = '.'

count_p1 = 0
while True:
    try:
        drop_sand(500, 0)
        count_p1 += 1
    except IndexError:
        break
print(count_p1)

reset_grid()

grid[max_y+2] = ['#'] * len(grid[max_y+2])
count_p2 = 0
while grid[0][500] != 'o':
    drop_sand(500, 0)
    count_p2 += 1
print(count_p2)
