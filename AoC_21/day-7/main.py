with open('./input.txt') as input:
    line = input.readline()
    positions = list(map(lambda x: int(x), line.split(',')))

def find_fuel_load(starting_positions, target):
    result = 0
    for pos in starting_positions:
        result += abs(target - pos)
    return result

def find_fuel_load_2(starting_positions, target):
    result = 0
    for pos in starting_positions:
        n = abs(target - pos)
        result += n*(n+1)/2
    return result

MAX = max(positions)
MIN = min(positions)

fuel_loads = []
for i in range(MIN, MAX+1):
    fuel_loads.append(find_fuel_load_2(positions, i))
print(min(fuel_loads))