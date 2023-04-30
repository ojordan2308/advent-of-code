from math import prod


INPUT_PATH = './input.txt'
TEST_INPUT_PATH = './test-input.txt'
HEXADECIMAL_CONVERSION = {hexadecimal: f'{i:04b}' for i, hexadecimal in enumerate('0123456789ABCDEF')}
TOTAL_VERSION = 0


def convert_input(puzzle_input_path = INPUT_PATH):
    with open(puzzle_input_path) as input:
        packets = input.readline()
    bin_packets = ''.join([HEXADECIMAL_CONVERSION[char] for char in packets])
    return bin_packets


def parse_literal(packets, i):

    literal_value_binary = ''
    prefix = packets[i]
    while prefix == '1':
        literal_value_binary += packets[i+1: i+5]
        i += 5
        prefix = packets[i]
    literal_value_binary += packets[i+1: i+5]
    i += 5
    return {"val": int(literal_value_binary, 2), "i": i}


def parse_operators(packets, i):
    values = []

    length_type_id = packets[i]

    if length_type_id == '0':
        sub_packets_length = int(packets[i+1:i+16], 2)
        i += 16
        res = parse_sub_packets_length(packets, sub_packets_length, i)
        #values.append(res["val"])
        values += res["val"]
        i = res["i"]

    elif length_type_id == '1':
        sub_packets_total = int(packets[i+1:i+12], 2)
        i += 12
        res = parse_sub_packets_total(packets, sub_packets_total, i)
        #values.append(res["val"])
        values += res["val"]
        i = res["i"]

    return {"val": values, "i": i}


def parse_sub_packets_length(packets, n, i):
    values = []
    max = i + n

    while i < max:
        res = parse_packets(packets, i)
        #values.append(res["val"])
        values += res["val"]
        i = res["i"]

    return {"val": values, "i": i}


def parse_sub_packets_total(packets, n, i):
    values = []
    while len(values) < n:
        res = parse_packets(packets, i)
        #values.append(res["val"])
        values += res["val"]
        i = res["i"]
    
    return {"val": values, "i": i}


def parse_packets(packets, i):
    values = []

    version = int(packets[i:i+3], 2)

    global TOTAL_VERSION
    TOTAL_VERSION += version

    type_id = int(packets[i+3:i+6], 2)
    i += 6

    if type_id == 4:
        res = parse_literal(packets, i)
        values.append(res["val"])
        i = res["i"]
    else:
        res = parse_operators(packets, i)
        values.append((type_id, res["val"]))
        #values += res["val"]
        i = res["i"]

    return {"val": values, "i": i}


def evaluate_packets(packet_values):
    total = 0
    sub = packet_values

    if sub[0] == 0:
        total += sum(map(
            lambda x: evaluate_packets(x) if isinstance(x, tuple) else x, sub[1]
            ))
    if sub[0] == 1:
        total += prod(map(
            lambda x: evaluate_packets(x) if isinstance(x, tuple) else x, sub[1]
            ))
    if sub[0] == 2:
        total += min(map(
            lambda x: evaluate_packets(x) if isinstance(x, tuple) else x, sub[1]
            ))
    if sub[0] == 3:
        total += max(map(
            lambda x: evaluate_packets(x) if isinstance(x, tuple) else x, sub[1]
            ))
    if sub[0] == 5:
        vals = list(map(lambda x: evaluate_packets(x) if isinstance(x, tuple) else x, sub[1]))
        total += 1 if vals[0] > vals[1] else 0
    if sub[0] == 6:
        vals = list(map(lambda x: evaluate_packets(x) if isinstance(x, tuple) else x, sub[1]))
        total += 1 if vals[0] < vals[1] else 0
    if sub[0] == 7:
        vals = list(map(lambda x: evaluate_packets(x) if isinstance(x, tuple) else x, sub[1]))
        total += 1 if vals[0] == vals[1] else 0
    return total


if __name__ == "__main__":
    parsed_packets = parse_packets(convert_input(), 0)

    print("======PART 1======")
    print(TOTAL_VERSION)

    print("======PART 2======")
    print(evaluate_packets(parsed_packets["val"][0]))
        