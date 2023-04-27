TEST_INPUT_PATH = './test-input.txt'
INPUT_PATH = './input.txt'
CORRUPT_VALUE = {')': 3, ']': 57, '}': 1197, '>': 25137}
INCOMPLETE_VALUE = {'(': 1, '[': 2, '{': 3, '<': 4}

def read_input(path_to_input):
    with open(path_to_input) as input:
        for line in input:
            line = line.rstrip('\n')
            while '{}' in line or '[]' in line or '()' in line or '<>' in line:
                line = line.replace('{}', '')
                line = line.replace('[]', '')
                line = line.replace('()', '')
                line = line.replace('<>', '')
            yield line

def find_corrupted_line_value(line):
    for char in line:
        if char in ')]}>':
            return CORRUPT_VALUE[char]
    return 0

def find_incomplete_line_value(line):
    score = 0
    for char in line[::-1]:
        score *= 5
        score += INCOMPLETE_VALUE[char]
    return score

if __name__ == "__main__":

    part1_total = 0
    part2_scores = []

    for line in read_input(INPUT_PATH):
        part1_val = find_corrupted_line_value(line)
        if part1_val:
            part1_total += part1_val
        else:
            part2_scores += [find_incomplete_line_value(line)]

    print(part1_total)
    print(sorted(part2_scores)[len(part2_scores)//2])