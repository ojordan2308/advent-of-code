class Position:
    def __init__(self, row, column, was_visited = False):
        self.row = row
        self.column = column
        self.was_visited = was_visited

    def __repr__(self):
        return f"({self.row}, {self.column})"

def move_head(dir, head_position):
    if dir == 'U':
        head_position = grid[head_position.row - 1][head_position.column]
    if dir == 'D':
        head_position = grid[head_position.row + 1][head_position.column]
    if dir == 'L':
        head_position = grid[head_position.row][head_position.column - 1]
    if dir == 'R':
        head_position = grid[head_position.row][head_position.column + 1]
    return head_position
        
def move_tail(knot_ahead, tail_position):
    tail_row = tail_position.row
    tail_column = tail_position.column
    head_row = knot_ahead.row
    head_column = knot_ahead.column
    
    if (tail_row - head_row) in [-1,0,1] and (tail_column - head_column) in [-1,0,1]:
        return tail_position
    
    if tail_row - head_row == 2:
        if tail_column == head_column:
            tail_position = grid[tail_row - 1][tail_column]
        elif tail_column - head_column > 0:
            tail_position = grid[tail_row - 1][tail_column - 1]
        elif head_column - tail_column > 0:
            tail_position = grid[tail_row - 1][tail_column + 1]
    
    elif head_row - tail_row == 2:
        if tail_column == head_column:
            tail_position = grid[tail_row + 1][tail_column]
        elif tail_column - head_column > 0:
            tail_position = grid[tail_row + 1][tail_column - 1]
        elif head_column - tail_column > 0:
            tail_position = grid[tail_row + 1][tail_column + 1]
    
    elif tail_column - head_column == 2:
        if tail_row == head_row:
            tail_position = grid[tail_row][tail_column - 1]
        elif tail_row - head_row > 0:
            tail_position = grid[tail_row - 1][tail_column - 1]
        elif head_row - tail_row > 0:
            tail_position = grid[tail_row + 1][tail_column - 1]
    
    elif head_column - tail_column == 2:
        if tail_row == head_row:
            tail_position = grid[tail_row][tail_column + 1]
        elif tail_row - head_row > 0:
            tail_position = grid[tail_row - 1][tail_column + 1]
        elif head_row - tail_row > 0:
            tail_position = grid[tail_row + 1][tail_column + 1] 
    
    tail_position.was_visited = True
    return tail_position

def move_knot(knot_ahead, knot):
    tail_row = knot.row
    tail_column = knot.column
    head_row = knot_ahead.row
    head_column = knot_ahead.column
    
    if (tail_row - head_row) in [-1,0,1] and (tail_column - head_column) in [-1,0,1]:
        return knot

    if tail_row - head_row == 2:
        if tail_column == head_column:
            knot = grid[tail_row - 1][tail_column]
        elif tail_column - head_column > 0:
            knot = grid[tail_row - 1][tail_column - 1]
        elif head_column - tail_column > 0:
            knot = grid[tail_row - 1][tail_column + 1]
    
    elif head_row - tail_row == 2:
        if tail_column == head_column:
            knot = grid[tail_row + 1][tail_column]
        elif tail_column - head_column > 0:
            knot = grid[tail_row + 1][tail_column - 1]
        elif head_column - tail_column > 0:
            knot = grid[tail_row + 1][tail_column + 1]
    
    elif tail_column - head_column == 2:
        if tail_row == head_row:
            knot = grid[tail_row][tail_column - 1]
        elif tail_row - head_row > 0:
            knot = grid[tail_row - 1][tail_column - 1]
        elif head_row - tail_row > 0:
            knot = grid[tail_row + 1][tail_column - 1]
    
    elif head_column - tail_column == 2:
        if tail_row == head_row:
            knot = grid[tail_row][tail_column + 1]
        elif tail_row - head_row > 0:
            knot = grid[tail_row - 1][tail_column + 1]
        elif head_row - tail_row > 0:
            knot = grid[tail_row + 1][tail_column + 1] 

    return knot

directions = []
with open('/Users/oliverjordan/AoC_22/day_9/input.txt') as input:
    for line in input:
        line = line.rstrip('\n')
        direction = line.replace(' ', '')
        directions.append(direction)

directions_test = ['R5', 'U8', 'L8', 'D3', 'R17', 'D10', 'L25', 'U20']

grid = []
for i in range(3001):
    row = []
    for j in range(3001):
        row.append(Position(i, j))
    grid.append(row)

if __name__ == '__main__':
    start = grid[1500][1500]
    start.head = True
    start.tail = True
    start.was_visited = True
    head_position = start
    one_position = start
    two_position = start
    three_position = start
    four_position = start
    five_position = start
    six_position = start
    seven_position = start
    eight_position = start
    tail_position = start

    for direction in directions:
        dir = direction[0]
        num_of_moves = int(direction[1:])
        i = 0
        while i < num_of_moves:
            head_position = move_head(dir, head_position)
            one_position = move_knot(head_position, one_position)
            two_position = move_knot(one_position, two_position)
            three_position = move_knot(two_position, three_position)
            four_position = move_knot(three_position, four_position)
            five_position = move_knot(four_position, five_position)
            six_position = move_knot(five_position, six_position)
            seven_position = move_knot(six_position, seven_position)
            eight_position = move_knot(seven_position, eight_position)
            tail_position = move_tail(eight_position, tail_position)
            i += 1
            #print(i, head_position, one_position, two_position, three_position,
                  #four_position, five_position, six_position, seven_position,
                  #eight_position, tail_position, tail_position.was_visited, i)

    print(grid[1497][1501].was_visited)
    count = 0
    for row in grid:
        for position in row:
            if position.was_visited is True:
                count += 1
    print(count)