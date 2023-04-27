NUMBERS = []
BOARDS = []

def check_for_winning_board(boards, numbers):
    winning_boards = []
    for board in boards:
        for row in board:
            if len(list(filter(lambda x: x in numbers, row))) == 5:
                winning_boards.append(board)
                continue
        for i in range(5):
            if len(list(filter(lambda x: x in numbers,
                               [board[j][i] for j in range(5)]))) == 5:
                winning_boards.append(board)
                continue
    if winning_boards:
        return winning_boards
    return False

def calculate_score(boards, numbers):
    winning_scores = []
    for board in boards:
        sum = 0
        multiplier = numbers[-1]
        board_numbers = [num for row in board for num in row]
        for num in board_numbers:
            if num not in numbers:
                sum += num
        winning_scores.append(sum*multiplier)
    return winning_scores

if __name__ == "__main__":
    with open('/Users/oliverjordan/AoC_21/day-4/input.txt') as input:
        lines = list(map(lambda x: x.rstrip('\n'), input.readlines()))

    NUMBERS += list(map(lambda x: int(x), lines[0].split(',')))

    for i in range(2, len(lines)-4, 6):
        board = [list(map(lambda x: int(x), lines[i+j].split())) for j in range(5)]
        BOARDS.append(board)
    
    while len(BOARDS) > 0:
        for i in range(1, len(NUMBERS)):
            nums = NUMBERS[:i]
            winning_boards = check_for_winning_board(BOARDS, nums)
            if winning_boards:
                print(calculate_score(winning_boards, nums))
                for board in winning_boards:
                    if board in BOARDS:
                        BOARDS.remove(board)
