from part_1 import instructions

SPRITE_POSITION = ['#','#','#','.','.','.','.','.','.','.',
                   '.','.','.','.','.','.','.','.','.','.',
                   '.','.','.','.','.','.','.','.','.','.',
                   '.','.','.','.','.','.','.','.','.','.']

def update_sprite_position(x):
    sprite_position = ['.','.','.','.','.','.','.','.','.','.',
                       '.','.','.','.','.','.','.','.','.','.',
                       '.','.','.','.','.','.','.','.','.','.',
                       '.','.','.','.','.','.','.','.','.','.']
    sprite_position[x-1] ='#'
    sprite_position[x-2] ='#'
    sprite_position[x] ='#'
    return sprite_position

X = 1
CYCLE = 0
INCREMENT = 0
screen = []

for i in range(len(instructions)):
    screen.append(SPRITE_POSITION[CYCLE%40])
    if i > 0:
        if instructions[i-1][:4]=='addx':
            CYCLE += 1
            screen.append(SPRITE_POSITION[CYCLE%40])
    if instructions[i] == 'noop':
        CYCLE += 1
    elif instructions[i][:4] == 'addx':
        CYCLE += 1
        X += int(instructions[i][5:])
        SPRITE_POSITION = update_sprite_position(X)
    
row_1 = ''.join(screen[:40])
row_2 = ''.join(screen[40:80])
row_3 = ''.join(screen[80:120])
row_4 = ''.join(screen[120:160])
row_5 = ''.join(screen[160:200])
row_6 = ''.join(screen[200:240])
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)
print(row_6)