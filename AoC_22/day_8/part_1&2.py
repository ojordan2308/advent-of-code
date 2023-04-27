class Tree:

    def __init__(self, height, row, column):
        self.height = int(height)
        self.row = row
        self.column = column
    
    def __repr__(self):
        return self.height


grid = []
with open('/Users/oliverjordan/AoC_22/day_8/input_8.txt') as input:
    row_num = 0
    for line in input:
        line = line.rstrip("\n")
        row = []
        column_num = 0
        for height in line:
            row.append(Tree(height, row_num, column_num))
            column_num += 1
        grid.append(row)
        row_num += 1


def calculate_scenic_score(tree):
    row = tree.row
    column = tree.column
    height = tree.height
    # scenic score left
    scenic_score_left = 1
    trees_left = grid[row][:column]
    num_left = len(trees_left)
    i = 1
    while i<num_left and trees_left[-i].height < height:
            scenic_score_left += 1
            i += 1
    # scenic score right
    scenic_score_right = 1
    trees_right = grid[row][column+1:]
    num_right = len(trees_right)
    j = 0
    while j<num_right-1 and trees_right[j].height < height:
            scenic_score_right += 1
            j += 1
    # scenic score up
    scenic_score_up = 1
    trees_up = []
    for i in range(row-1, -1, -1):
        trees_up.append(grid[i][column].height)
    k = 0
    while k<len(trees_up)-1 and trees_up[k] < height:
            scenic_score_up += 1
            k += 1
    # scenic score down
    scenic_score_down = 1
    trees_down = []
    row_index = row + 1
    while row_index < 99:
        trees_down.append(grid[row_index][column].height)
        row_index += 1
    l = 0
    while l<len(trees_down)-1 and trees_down[l] < height:
            scenic_score_down += 1
            l += 1
    return scenic_score_down*scenic_score_left*scenic_score_right*scenic_score_up

max = 0
for i in range(1, 98):
    for j in range(1, 98):
        if calculate_scenic_score(grid[i][j]) > max:
            max = calculate_scenic_score(grid[i][j])
print(max)

def is_visible(tree):
    row = tree.row
    column = tree.column
    height = tree.height
    # visible from the left
    l_max_intervening_tree = max(list(map(lambda x: x.height, grid[row][:column])))
    if l_max_intervening_tree < height:
        return True
    # visible from the right
    r_max_intervening_tree = max(list(map(lambda x: x.height, grid[row][column+1:])))
    if r_max_intervening_tree < height:
        return True
    # visible from front
    trees_in_front = []
    i = row + 1
    while i<=98:
        trees_in_front.append(grid[i][column].height)
        i+=1
    if max(trees_in_front) < height:
        return True
    # visible from back
    trees_behind = []
    j = row - 1
    while j>=0:
        trees_behind.append(grid[j][column].height)
        j-=1
    if max(trees_behind) < height:
        return True
    return False

total_visible = 392
for i in range(1, 98):
    for j in range(1, 98):
        if is_visible(grid[i][j]):
            total_visible += 1

print(total_visible)