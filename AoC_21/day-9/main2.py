from math import prod

class Node:
    def __init__(self, row, column, value):
        self.row = row
        self.column = column
        self.value = value
        self.neighbours = []
        self.basin_low_point = None

    def __repr__(self):
        return str(self.value)


def find_neighbours_and_low_points(node, grid):
    row, column = node.row, node.column
    value = node.value
    nrow = len(grid)
    ncolumn = len(grid[row])
    # check left
    if column > 0:
        l_neighbour = grid[row][column-1]
        if l_neighbour.value < value:
            node.neighbours.append(l_neighbour)
    # check right
    if column < ncolumn-1:
        r_neighbour = grid[row][column+1]
        if r_neighbour.value < value:
            node.neighbours.append(r_neighbour)
    # check up
    if row > 0:
        u_neighbour = grid[row-1][column]
        if u_neighbour.value < value:
            node.neighbours.append(u_neighbour)
    # check down
    if row < nrow-1:
        d_neighbour = grid[row+1][column]
        if d_neighbour.value < value:
            node.neighbours.append(d_neighbour)

    if not node.neighbours:
        return True
    return False

def which_basin(node, low_points):
    found_basin_low_point = False
    next = node.neighbours
    while not found_basin_low_point:
        for l in low_points:
            if l in next:
                found_basin_low_point = True
                node.basin_low_point = l
        next = [neighbour for n in next for neighbour in n.neighbours]


if __name__ == "__main__":
    
    GRID = []
    with open('./input.txt') as input:
        i = 0
        for line in input:
            line = line.rstrip('\n')
            row = [Node(i, j, int(line[j])) for j in range(len(line))]
            GRID.append(row)
            i += 1
    
    LOW_POINTS = []
    for row in GRID:
        for node in row:
            if find_neighbours_and_low_points(node, GRID):
                LOW_POINTS.append(node)

    for row in GRID:
        for node in row:
            if node.value != 9 and node not in LOW_POINTS:
                which_basin(node, LOW_POINTS)

    BASIN_SIZES = []
    for point in LOW_POINTS:
        size = 1
        for row in GRID:
            for node in row:
                if node.basin_low_point == point:
                    size += 1
        BASIN_SIZES.append(size)
    
    print(prod(sorted(BASIN_SIZES)[-3:]))