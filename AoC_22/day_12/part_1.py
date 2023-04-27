ALPHA = 'abcdefghijklmnopqrstuvwxyz'

class Node:
    def __init__(self, level, end = False, start = False):
        self.level = level
        self.connects = []
        self.row = 0
        self.column = 0
        self.end = end
        self.start = start
    
    def __repr__(self):
        return f"{self.row, self.column}"

grid = []
start_options = []
with open('/Users/oliverjordan/AoC_22/day_12/input_12.txt') as input:
    for line in input:
        line = line.rstrip('\n')
        row = []
        for char in line:
            if char == 'S':
                start_node = Node(0, start=True)
                row.append(start_node)
                start_options.append(start_node)
            elif char == 'a':
                potential_start_node = Node(0)
                row.append(potential_start_node)
                start_options.append(potential_start_node)
            elif char == 'E':
                row.append(Node(25, end = True))
            else:
                row.append(Node(ALPHA.index(char)))
        grid.append(row)

rows = len(grid)
columns = len(grid[0])

def find_neighbours(i, j):
    node = grid[i][j]
    node.row = i
    node.column = j
    if i > 0:
        above_neighbour = grid[i-1][j]
        if above_neighbour.level <= node.level + 1:
            node.connects.append(above_neighbour)
    if i < rows - 1:
        below_neighbour = grid[i+1][j]
        if below_neighbour.level <= node.level + 1:
            node.connects.append(below_neighbour)
    if j > 0:
        left_neighbour = grid[i][j-1]
        if left_neighbour.level <= node.level + 1:
            node.connects.append(left_neighbour)
    if j < columns - 1:
        right_neighbour = grid[i][j+1]
        if right_neighbour.level <= node.level + 1:
            node.connects.append(right_neighbour)
    #print(node.connects)

for i in range(rows):
    for j in range(columns):
        #if grid[i][j].start:
            #start = grid[i][j]
        if grid[i][j].end:
            end = grid[i][j]
        find_neighbours(i, j)

path_lengths = []
og_start_distance = 0
for s_node in start_options:
    start = s_node
    if start.start:
        is_og_start = True
    else:
        is_og_start = False

    steps = 0
    reached_end = True
    explored_nodes = []
    current_level = [start]

    while end not in current_level:
        steps += 1
        next_level = []
        for node in current_level:
            for neighbour in node.connects:
                if neighbour not in explored_nodes:
                    next_level.append(neighbour)
                    explored_nodes.append(neighbour)
        if not next_level:
            reached_end = False
            break
        current_level = next_level

    if reached_end:
        path_lengths.append(steps)
    if is_og_start:
        og_start_distance = steps

print(og_start_distance)
print(min(path_lengths))