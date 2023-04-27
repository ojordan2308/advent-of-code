with open('/Users/oliverjordan/AoC_22/day_6/input_6.txt') as input:
    signal = ''
    for line in input:
        for char in line:
            signal += line

def find_index(signal):
    j = 0
    for i in range(4, len(signal)):
        if len(list(set(signal[j:i]))) == 4:
            return i
        j += 1

#print(find_index(signal))

def find_index_message_marker(signal):
    j = 0
    for i in range(14, len(signal)):
        if len(list(set(signal[j:i]))) == 14:
            return i
        j += 1

print(find_index_message_marker(signal))