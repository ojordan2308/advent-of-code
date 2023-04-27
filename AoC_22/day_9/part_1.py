class Position:
    def __init__(self, row, column, was_visited = False):
        self.row = row
        self.column = column
        self.was_visited = was_visited

    def __repr__(self):
        return f"({self.row}, {self.column})"

grid = []
for i in range(3001):
    row = []
    for j in range(3001):
        row.append(Position(i, j))
    grid.append(row)

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
        
def move_tail(head_position, tail_position):
    tail_row = tail_position.row
    tail_column = tail_position.column
    head_row = head_position.row
    head_column = head_position.column
    
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


directions = []
with open('/Users/oliverjordan/AoC_22/day_9/input_9.txt') as input:
    for line in input:
        line = line.rstrip('\n')
        direction = line.replace(' ', '')
        directions.append(direction)

#directions_test = ['R4', 'U4', 'L3', 'D1', 'R4', 'D1', 'L5', 'R2']

if __name__ == '__main__':
    start = grid[1500][1500]
    start.was_visited = True
    head_position = start
    tail_position = start

    for direction in directions:
        dir = direction[0]
        num_of_moves = int(direction[1:])
        i = 0
        while i < num_of_moves:
            head_position = move_head(dir, head_position)
            tail_position = move_tail(head_position, tail_position)
            i += 1

    count = 0
    for row in grid:
        for position in row:
            if position.was_visited is True:
                count += 1
    print(count)