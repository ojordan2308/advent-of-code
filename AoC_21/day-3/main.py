diag_report = []
with open('/Users/oliverjordan/AoC_21/day-3/input.txt') as input:
    for line in input:
        diag_report.append(line.rstrip('\n'))

gamma_rate = ''
epsilon_rate = ''

for i in range(len(diag_report[0])):
    count_1 = 0
    count_0 = 0
    for line in diag_report:
        if line[i] == '1':
            count_1 += 1
        else:
            count_0 += 1
    if count_1 > count_0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

og_rating = diag_report
while len(og_rating) > 1:
    for i in range(len(diag_report[0])):
        count_1 = 0
        count_0 = 0
        for line in og_rating:
            if line[i] == '1':
                count_1 += 1
            else:
                count_0 += 1
        if count_1 > count_0:
            og_rating = list(filter(lambda x: x[i] == '1', og_rating))
        elif count_1 < count_0:
            og_rating = list(filter(lambda x: x[i] == '0', og_rating))
        else:
            og_rating = list(filter(lambda x: x[i] == '1', og_rating))
        if len(og_rating) == 1: oxygen_rating = int(og_rating[0], 2)
cs_rating = diag_report
while len(cs_rating) > 1:
    for i in range(len(diag_report[0])):
        count_1 = 0
        count_0 = 0
        for line in cs_rating:
            if line[i] == '1':
                count_1 += 1
            else:
                count_0 += 1
        if count_1 < count_0:
            cs_rating = list(filter(lambda x: x[i] == '1', cs_rating))
        elif count_1 > count_0:
            cs_rating = list(filter(lambda x: x[i] == '0', cs_rating))
        else:
            cs_rating = list(filter(lambda x: x[i] == '0', cs_rating))
        if len(cs_rating) == 1: co2_rating = int(cs_rating[0], 2)

print(oxygen_rating*co2_rating)