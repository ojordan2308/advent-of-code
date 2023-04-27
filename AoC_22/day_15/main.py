import re

SENSORS = []
BEACONS = []
DISTANCES = []
RANGES = {}
MAX = 4000000
TEST_MAX = 20

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

def find_sensor_ranges(sensor, distance, ranges):
    x, y = sensor
    min_y = 0 if y-distance < 0 else y-distance
    max_y = MAX if y+distance > MAX else y+distance
    for j in range(min_y, max_y+1):
        if j <= y:
            x_min = 0 if x+y-j-distance < 0 else x+y-j-distance
            x_max = MAX if x-y+j+distance > MAX else x-y+j+distance
            x_interval = (x_min, x_max)
            if j in ranges:
                ranges[j].append(x_interval)
            else:
                ranges[j] = [x_interval]
        else:
            x_min = 0 if x-y+j-distance < 0 else x-y+j-distance
            x_max = MAX if x+y-j+distance > MAX else x+y-j+distance
            x_interval = (x_min, x_max)
            if j in ranges:
                ranges[j].append(x_interval)
            else:
                ranges[j] = [x_interval]
    return ranges

def merge_intervals(intervals):
    merged_intervals = []
    for start, end in sorted(intervals):
        if merged_intervals and merged_intervals[-1][1] >= start - 1:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
        else:
            merged_intervals.append([start, end])
    return merged_intervals

def tuning_frequency(x, y):
    return x*4000000 + y

def find_missing_coord_in_ranges(ranges):
    for y, intervals in ranges.items():
        merged_intervals = merge_intervals(intervals)
        if len(merged_intervals) == 2:
            x = merged_intervals[0][1] + 1
            return tuning_frequency(x, y)


if __name__ == "__main__":

    with open('/Users/oliverjordan/AoC_22/day_15/input.txt') as input:
        for line in input:
            x_coords = list(map(lambda x: int(x), re.findall('(?<=x=)-?\d*', line)))
            y_coords = list(map(lambda x: int(x), re.findall('(?<=y=)-?\d*', line)))

            [sensor, beacon] = zip(x_coords, y_coords)
            distance = manhattan_distance(*sensor, *beacon)

            SENSORS.append(sensor)
            BEACONS.append(beacon)
            DISTANCES.append(distance)

    for sensor, distance in zip(SENSORS, DISTANCES):
        find_sensor_ranges(sensor, distance, RANGES)
    print(find_missing_coord_in_ranges(RANGES))
    
    
    """imposible_beacon_coords = []
    for k in range(len(SENSORS)):
        sensor = SENSORS[k]
        distance = DISTANCES[k]
        imposible_beacon_coords += find_points_in_range(sensor, distance)
    a = filter(lambda x: x[1] == TARGET_Y and x not in [*BEACONS, *SENSORS],
               imposible_beacon_coords)
    print(len(set(a)))"""

    """invalid_beacon_coords = []
    for i in range(NEG_OFFSET, POS_OFFSET+1):
        coord = (i, TARGET_Y)
        if coord in SENSORS:
            continue
        if coord in BEACONS:
            continue
        for j in range(len(SENSORS)):
            if manhattan_distance(*SENSORS[j], *coord) <= DISTANCES[j]:
                invalid_beacon_coords.append(coord)
    print(len(list(set(invalid_beacon_coords))))"""

    """impossible_spots = [*SENSORS, *BEACONS]
    for i in range(len(SENSORS)):
        sensor_x, sensor_y = SENSORS[i]
        print(sensor_x, sensor_y)
        distance = DISTANCES[i]
        for x in range(sensor_x-distance, sensor_x+distance+1):
            for y in range(sensor_y-distance, sensor_y+distance+1):
                print(x, y)
                if manhattan_distance(sensor_x, sensor_y, x, y) <= distance:
                    impossible_spots.append((x, y))
    
    for i in range(4000000):
        for j in range(4000000):
            if (i, j) not in impossible_spots:
                print(tuning_frequency(i, j, 4000000))"""

    """for i in range(4000000):
        for j in range(4000000):
            coord = (i, j)
            if coord in SENSORS:
                continue
            if coord in BEACONS:
                continue
            in_range_of_sensor = False
            for k in range(len(SENSORS)):
                if manhattan_distance(*SENSORS[k], *coord) <= DISTANCES[k]:
                    in_range_of_sensor = True
                    break
            if not in_range_of_sensor:
                print(f"RESULT: {tuning_frequency(*coord, 4000000)}")
                break"""

