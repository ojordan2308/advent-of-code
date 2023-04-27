TEST_INPUT_PATH = './test-input.txt'
INPUT_PATH = './input.txt'
OCTOPUS_GRID = []


class DumboOctopus:
    def __init__(self, row, column, energy_level):
        self.row = row
        self.column = column
        self.energy_level = energy_level
        self.flash_count = 0
        self.has_flashed_this_step = False
    
    def __repr__(self):
        return str(self.energy_level)
    
    def check_energy_level(self):
        if not self.has_flashed_this_step:
            if self.energy_level > 9:
                self.has_flashed_this_step = True
                self.flash_count += 1
                self.flash()

    def flash(self, grid = OCTOPUS_GRID):
        n_row = len(grid)
        n_column = len(grid[self.row])
        # check above
        if self.row > 0:
            above_octopus = grid[self.row-1][self.column]
            above_octopus.energy_level += 1
            above_octopus.check_energy_level()
            # check above left and above right
            if self.column > 0:
                above_left_octopus = grid[self.row-1][self.column-1]
                above_left_octopus.energy_level += 1
                above_left_octopus.check_energy_level()
            if self.column < n_column-1:
                above_right_octopus = grid[self.row-1][self.column+1]
                above_right_octopus.energy_level += 1
                above_right_octopus.check_energy_level()
        # check below
        if self.row < n_row-1:
            below_octopus = grid[self.row+1][self.column]
            below_octopus.energy_level += 1
            below_octopus.check_energy_level()
            # check below left and below right
            if self.column > 0:
                below_left_octopus = grid[self.row+1][self.column-1]
                below_left_octopus.energy_level += 1
                below_left_octopus.check_energy_level()
            if self.column < n_column-1:
                below_right_octopus = grid[self.row+1][self.column+1]
                below_right_octopus.energy_level += 1
                below_right_octopus.check_energy_level()
        # check left
        if self.column > 0:
            left_octopus = grid[self.row][self.column-1]
            left_octopus.energy_level += 1
            left_octopus.check_energy_level()
        # check right
        if self.column < n_column-1:
            right_octopus = grid[self.row][self.column+1]
            right_octopus.energy_level += 1
            right_octopus.check_energy_level()


def reset_flash_step_bool(grid = OCTOPUS_GRID):
    for row in grid:
        for octopus in row:
            octopus.has_flashed_this_step = False

def reset_energy_levels_post_flash(grid = OCTOPUS_GRID):
    for row in grid:
        for octopus in row:
            if octopus.has_flashed_this_step:
                octopus.energy_level = 0

def check_energy_levels(grid = OCTOPUS_GRID):
    for row in grid:
        for octopus in row:
            octopus.check_energy_level()

def increment_energy_levels(grid = OCTOPUS_GRID):
    for row in grid:
        for octopus in row:
            octopus.energy_level += 1

def count_flashes(grid = OCTOPUS_GRID):
    total = 0
    for row in grid:
        for octopus in row:
            total += octopus.flash_count
    return total

def reset_flash_counts(grid = OCTOPUS_GRID):
    for row in grid:
        for octopus in row:
            octopus.flash_count = 0


if __name__ == "__main__":
    
    with open(INPUT_PATH) as input:
        row_num = 0
        for line in input:
            line = line.rstrip('\n')
            row = list(map(lambda x: DumboOctopus(row_num, x[0], int(x[1])),
                           [octopus for octopus in enumerate(line)]))
            OCTOPUS_GRID.append(row)
            row_num += 1
    

    #for step in range(100):
        #increment_energy_levels()
        #check_energy_levels()
        #reset_energy_levels_post_flash()
        #reset_flash_step_bool()

    #print(count_flashes())

    total_number_of_octopi = len(OCTOPUS_GRID) * len(OCTOPUS_GRID[0])
    all_octopus_flash = False
    step = 1
    while not all_octopus_flash:
        increment_energy_levels()
        check_energy_levels()
        if count_flashes() == total_number_of_octopi:
            all_octopus_flash = True
            print(step)
        reset_energy_levels_post_flash()
        reset_flash_step_bool()
        reset_flash_counts()
        step += 1
