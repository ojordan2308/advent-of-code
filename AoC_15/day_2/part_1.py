presents = []
with open("/Users/oliverjordan/AoC/2015/day_2/input_2.txt") as input:
    for line in input:
        line = line.rstrip('\n')
        dimensions = list(map(lambda x: int(x), line.split('x')))
        presents.append(dimensions)

def required_wrapping_paper(dimensions):
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    areas = [l*w, l*h, w*h]
    size = 0
    for area in areas:
        size += 2*area
    return size + min(areas)

def required_ribbon(dimensions):
    dimensions = sorted(dimensions)
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    return l*w*h + 2*(l+w)


paper_total = 0
ribbon_total = 0
for present in presents:
    paper_total += required_wrapping_paper(present)
    ribbon_total += required_ribbon(present)

print(paper_total, ribbon_total)