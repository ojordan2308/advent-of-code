# A, X = Rock / B, Y = Paper / C, Z = Scissors
translate = {'X': 'A', 'Y': 'B', 'Z': 'C'}
beats = {'A': 'C', 'B': 'A', 'C': 'B'}
points = {'A': 1, 'B': 2, 'C': 3}

def calculate_my_points(str):
    str = str.replace(str[1], translate[str[1]])
    score = 0
    if beats[str[1]] == str[0]:
        score += 6
    elif not beats[str[0]] == str[1]:
        score += 3
    score += points[str[1]]
    return score
    
games = []
with open('/Users/oliverjordan/AoC_22/day_2/input_2.txt') as input:
    for line in input:
        game = line[:3].replace(' ', '')
        games.append(game)

points_per_game = list(map(calculate_my_points, games))
my_points_total = sum(points_per_game)
print(my_points_total)