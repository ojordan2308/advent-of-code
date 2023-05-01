import re


INPUT_PATH = './input.txt'
TEST_INPUT_PATH = './test-input.txt'


def get_target_area(puzzle_input_path = INPUT_PATH):
    with open(puzzle_input_path) as input:
        data = input.readline()
        target_x = tuple(map(lambda x: int(x),
                             re.search("(?<=x=)-?\d*\.\.-?\d*", data).group().split('..')))
        target_y = tuple(map(lambda x: int(x),
                             re.search("(?<=y=)-?\d*\.\.-?\d*", data).group().split('..')))
    
    return [target_x, target_y]


def test_point_in_target_area(x, y, x_range, y_range):
    x_min, x_max = x_range
    y_min, y_max = y_range
    if x < x_min or x > x_max:
        return False 
    if y < y_min or y > y_max:
        return False
    return True


def test_velocity_trajectory(initial_velocity, x_range, y_range):
    u, v = initial_velocity
    u += 1
    v += 1
    x, y = 0, 0
    highest_point_reached = 0
    x_min, x_max = x_range
    y_min, y_max = y_range
    while x <= x_max and y >= y_min:
        u = u - 1 if u > 0 else 0
        v -= 1
        x += u
        y += v

        if y > highest_point_reached:
            highest_point_reached = y

        if test_point_in_target_area(x, y, x_range, y_range):
            return True, (x, y), highest_point_reached
    return False, (x, y)


if __name__ == "__main__":
    x_range, y_range = get_target_area()
    
    highest_point_reached = 0
    count = 0
    for i in range(500):
        for j in range(-1000, 1000):
            res = test_velocity_trajectory((i, j), x_range, y_range)
            if res[0]:
                count += 1
                if res[2] > highest_point_reached:
                    highest_point_reached = res[2]

    print("======PART 1======")
    print(highest_point_reached)
    print("======PART 2======")
    print(count)
