with open("/Users/oliverjordan/2015/day_1/input_1.txt") as input:
    floor = 0
    for line in input:
        position = 1
        for char in line:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            if floor < 0:
                print(position)
                break
            position += 1


print(floor)