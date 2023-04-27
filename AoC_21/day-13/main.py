INPUT_PATH = './input.txt'
TEST_INPUT_PATH = './test-input.txt'
PAPER = []
DOT_POSITIONS = []
FOLD_INSTRUCTIONS = []


def get_dots_and_folds(puzzle_input_path = INPUT_PATH,
                       dot_positions = DOT_POSITIONS,
                       fold_instructions = FOLD_INSTRUCTIONS):
    with open(puzzle_input_path) as input:
        for line in input:
            line = line.rstrip('\n')
            if ',' in line:
                coord = tuple(map(lambda x: int(x), line.split(',')))
                dot_positions.append(coord)
            elif line:
                fold = tuple(line.split()[-1].split('='))
                fold_instructions.append(fold)

def draw_dots(paper = PAPER, dot_positions = DOT_POSITIONS):
    paper_length = max([pos[1] for pos in dot_positions]) + 1
    paper_width = max([pos[0] for pos in dot_positions]) + 1
    for j in range(paper_length):
        paper.append(['.'] * paper_width)
    for x, y in dot_positions:
        paper[y][x] = '#'

def pay_per_view(paper):
    for row in paper:
        print(''.join(row))

def fold(axis, n, paper):
    if axis == 'x':
        left, right = [row[:n] for row in paper], [row[n+1:][::-1] for row in paper]
        l_len, r_len = len(left), len(right)
        folded_paper = []

        if l_len == r_len:
            for l_row, r_row in zip(left, right):
                new_row = []
                for i in range(len(l_row)):
                    if l_row[i] == '.' and r_row[i] == '.':
                        new_row.append('.')
                    else:
                        new_row.append('#')
                folded_paper.append(new_row)
            return folded_paper

        if l_len < r_len:
            folded_paper += [row[:-l_len] for row in right]
            for l_row, r_row in zip(left, right[-l_len:]):
                new_row = []
                for i in range(len(l_row)):
                    if l_row[i] == '.' and r_row[i] == '.':
                        new_row.append('.')
                    else:
                        new_row.append('#')
                folded_paper.append(new_row)
            return folded_paper

        if l_len > r_len:
            folded_paper += [row[:-r_len] for row in left]
            for l_row, r_row in zip(left[-r_len:], right):
                new_row = []
                for i in range(len(l_row)):
                    if l_row[i] == '.' and r_row[i] == '.':
                        new_row.append('.')
                    else:
                        new_row.append('#')
                folded_paper.append(new_row)
            return folded_paper

    elif axis == 'y':
        up, down = paper[:n], paper[n+1:][::-1]
        u_len, d_len = len(up), len(down)
        folded_paper = []

        if u_len == d_len:
            for u_row, d_row in zip(up, down):
                new_row = []
                for i in range(len(u_row)):
                    if u_row[i] == '.' and d_row[i] == '.':
                        new_row.append('.')
                    else:
                        new_row.append('#')
                folded_paper.append(new_row)
            return folded_paper

        if u_len < d_len:
            folded_paper += down[:-u_len]
            for u_row, d_row in zip(up, down[-u_len:]):
                new_row = []
                for i in range(len(u_row)):
                    if u_row[i] == '.' and d_row[i] == '.':
                        new_row.append('.')
                    else:
                        new_row.append('#')
                folded_paper.append(new_row)
            return folded_paper

        if u_len > d_len:
            folded_paper += up[:-d_len]
            for u_row, d_row in zip(up[-d_len:], down):
                new_row = []
                for i in range(len(u_row)):
                    if u_row[i] == '.' and d_row[i] == '.':
                        new_row.append('.')
                    else:
                        new_row.append('#')
                folded_paper.append(new_row)
            return folded_paper
        
def count_visible_hashtags(paper):
    count = 0
    for row in paper:
        for dot in row:
            if dot == '#':
                count +=1
    print(count)

if __name__ == "__main__":
    get_dots_and_folds()
    draw_dots()
    for axis, n in FOLD_INSTRUCTIONS:
        PAPER = fold(axis, int(n), PAPER)
        if (axis, n) == FOLD_INSTRUCTIONS[0]:
            print('========Part 1========')
            count_visible_hashtags(PAPER)
    print('========Part 2========')
    pay_per_view(PAPER)
    
    