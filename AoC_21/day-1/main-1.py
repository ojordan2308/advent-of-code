depth = []
with open('/Users/oliverjordan/AoC_21/day-1/input.txt') as input:
    for line in input:
        line = line.rstrip('\n')
        depth.append(int(line))

count_p1 = 0
for i in range(1, len(depth)):
    if depth[i] > depth[i-1]:
        count_p1 += 1
print(count_p1)

count_p2 = 0
for i in range(2, len(depth)-1):
    j = i+1
    right = depth[j:j-3:-1]
    left = (depth[i:i-3:-1] if i!=2 else depth[0:3])
    if sum(right) > sum(left):
        count_p2 += 1
print(count_p2)