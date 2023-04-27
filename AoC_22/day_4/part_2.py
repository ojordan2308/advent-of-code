from part_1 import pairs, completely_contain

def overlap(list):
    if list[0] <= list[2] and list[1] >= list[2]:
        return True
    if list[0] <= list[3] and list[1] >= list[3]:
        return True
    if completely_contain(list):
        return True
    return False

overlapping_pairs = list(filter(overlap, pairs))
print(len(overlapping_pairs))