# A = Rock / B = Paper / C = Scissors , X = Lose / Y = Draw / Z = Win
from part_1 import beats, games, points

def calculate_my_points(str):
    score = 0
    if str[1] == 'X':
        str = str.replace('X', beats[str[0]])
    elif str[1] == 'Y':
        str = str.replace('Y', str[0])
        score += 3
    else:
        str = str.replace('Z', list(beats.keys())[list(beats.values()).index(str[0])])
        score += 6
    score += points[str[1]]
    return score
    
points_per_game = list(map(calculate_my_points, games))
my_points_total = sum(points_per_game)
print(my_points_total)
