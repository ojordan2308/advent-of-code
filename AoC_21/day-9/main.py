def is_low_point(row, column, grid):
    point  = grid[row][column]
    nrow = len(grid)
    ncolumn = len(grid[row])
    # check left
    if column > 0:
        if grid[row][column-1] <= point:
            return False
    # check right
    if column < ncolumn-1:
        if grid[row][column+1] <= point:
            return False
    # check up
    if row > 0:
        if grid[row-1][column] <= point:
            return False
    # check down
    if row < nrow-1:
        if grid[row+1][column] <= point:
            return False
    return True


if __name__ == "__main__":

    GRID = []
    with open('./test-input.txt') as input:
        for line in input:
            line = line.rstrip('\n')
            row = list(map(lambda x: int(x), [num for num in line]))
            GRID.append(row)

    low_points = []
    nrow = len(GRID)
    ncolumn = len(GRID[0])
    for i in range(nrow):
        for j in range(ncolumn):
            if is_low_point(i, j, GRID):
                low_points.append(GRID[i][j]) 
    print(sum(low_points) + len(low_points))

