from heapq import heapify, heappop, heappush

TEST_INPUT_PATH = './test-input.txt'
INPUT_PATH = './input.txt'


class Chiton:

    def __init__(self, row, column, risk_level):
        self.row = row
        self.column = column
        self.risk_level = risk_level
        self.connects = []

    def __lt__(self, other):
        return risk_from_start[self] < risk_from_start[other]

    def __repr__(self):
        return f"({self.row}, {self.column})"
    
    def increment_risk(self, n, row_length, col_length, same_row = False, same_col = False):
        new_risk = (self.risk_level + n) % 9
        if new_risk == 0:
            new_risk = 9
        if same_row:
            new_row = self.row
            new_column = self.column + n*row_length
        if same_col:
            new_row = self.row + n*col_length
            new_column = self.column
        return Chiton(new_row, new_column, new_risk)

    @classmethod
    def get_cavern(self, puzzle_input_path = INPUT_PATH):
        cavern = []

        with open(puzzle_input_path) as input:
            row_num = 0
            for line in input:
                line = line.rstrip('\n')
                row = [Chiton(row_num, column_num, int(risk_level)) for column_num, risk_level in enumerate(line)]
                cavern.append(row)
                row_num += 1
        
        return cavern

    @classmethod
    def connect_chitons(self, cavern):
        n_rows = len(cavern)
        n_columns = len(cavern[0])
        for row in cavern:
            for chiton in row:
                row_num = chiton.row
                column_num = chiton.column
                if row_num > 0:
                    chiton.connects.append(cavern[row_num-1][column_num])
                if row_num < n_rows - 1:
                    chiton.connects.append(cavern[row_num+1][column_num])
                if column_num > 0:
                    chiton.connects.append(cavern[row_num][column_num-1])
                if column_num < n_columns-1:
                    chiton.connects.append(cavern[row_num][column_num+1])

    @classmethod
    def get_big_cavern(self, cavern):
        row_length = len(cavern[0])
        col_length = len(cavern)
    
        big_cavern = []
        for row in cavern:
            new_row = row + list(map(lambda x: x.increment_risk(1, row_length, col_length, same_row = True), row)) \
                          + list(map(lambda x: x.increment_risk(2, row_length, col_length, same_row = True), row)) \
                          + list(map(lambda x: x.increment_risk(3, row_length, col_length, same_row = True), row)) \
                          + list(map(lambda x: x.increment_risk(4, row_length, col_length, same_row = True), row))
            big_cavern.append(new_row)
            
        big_cavern = big_cavern + [list(map(lambda x: x.increment_risk(1, row_length, col_length, same_col = True), row))
                                   for row in big_cavern] \
                                + [list(map(lambda x: x.increment_risk(2, row_length, col_length, same_col = True), row))
                                  for row in big_cavern] \
                                + [list(map(lambda x: x.increment_risk(3, row_length, col_length, same_col = True), row))
                                  for row in big_cavern] \
                                + [list(map(lambda x: x.increment_risk(4, row_length, col_length, same_col = True), row))
                                  for row in big_cavern] \

        return big_cavern


if __name__ == "__main__":

    cavern = Chiton.get_big_cavern(Chiton.get_cavern(puzzle_input_path=TEST_INPUT_PATH))
    Chiton.connect_chitons(cavern)

    n_rows = len(cavern)
    n_columns = len(cavern[0])

    start = cavern[0][0]
    end = cavern[n_rows-1][n_columns-1]
    end.connects = []

    risk_from_start = {chiton: 1000000 for row in cavern for chiton in row}
    risk_from_start[start] = 0

    iteration_num = 0
    next_chitons = [(start, iteration_num)]
    heapify(next_chitons)
    visited = []

    while next_chitons:
        iteration_num += 1
        #next_chitons = sorted(next_chitons, key=lambda chiton: risk_from_start[chiton])
        #current = next_chitons.pop(0)
        current = heappop(next_chitons)[0]
        for chiton in current.connects:
            path_risk_level = risk_from_start[current] + chiton.risk_level
            if path_risk_level < risk_from_start[chiton]:
                risk_from_start[chiton] = path_risk_level
            if chiton not in visited and chiton not in map(lambda x: x[0], next_chitons):
                #next_chitons.append(chiton)
                heappush(next_chitons, (chiton, iteration_num))
        visited.append(current)

    print(risk_from_start[end])

# who needs a grid
# A* algorithm ?
