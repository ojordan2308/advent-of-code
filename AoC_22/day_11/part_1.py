from math import prod

class Monkey:
    def __init__(self, id, items, operation, test, if_true, if_false):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.count = 0

    def inspect(self, worry_level):
        if 'old' in self.operation:
            return worry_level ** 2
        if self.operation[0] == '+':
            return worry_level + int(self.operation[1:])
        if self.operation[0] == '*':
            return worry_level * int(self.operation[1:])
    
    def condition(self, worry_level):
        if worry_level % self.test == 0:
            return True
        return False

    def throw(self, target, worry_level):
        target.items.append(worry_level)

monkey_stuff = []
with open("/Users/oliverjordan/AoC_22/day_11/input_11.txt") as input:
    monkey = []
    for line in input:
        line = line.rstrip('\n').strip()
        if line == '':
            continue
        monkey.append(line)
        if len(monkey) == 6:
            monkey_stuff.append(monkey)
            monkey = []
    
monkeys = []
for monkey in monkey_stuff:
    id = int(monkey[0][-2])
    items_str = monkey[1][16:].replace(' ', '').split(',')
    items = list(map(lambda x: int(x), items_str))
    o_index = monkey[2].find('old')
    operation = monkey[2][o_index+3:].replace(' ','')
    t_index = monkey[3].find('by')
    test = int(monkey[3][t_index+2:])
    if_true = int(monkey[4][-1])
    if_false = int(monkey[5][-1])
    monkeys.append(Monkey(id, items, operation, test, if_true, if_false))

def remainder_theorem(x: int, n: list[int]) -> int:
    # x is current worry level and n is a list of each monkeys 'test' value
    b = [x - ((x//num) * num) if x > num else x for num in n]
    # b is a list of worry level mod each 'test' value
    result = 0
    for i in range(len(b)):
        N = prod([num for num in n if n.index(num)!=i])
        result += b[i] * N * pow(N, -1, n[i])
    return result

#for i in range(20): part1
for i in range(10000):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop(0)
            monkey.count += 1
            worry_level = item
            worry_level = monkey.inspect(worry_level)
            #worry_level = worry_level//3 part1
            worry_level = remainder_theorem(worry_level, [m.test for m in monkeys])
            if monkey.condition(worry_level):
                monkey.throw(monkeys[monkey.if_true], worry_level)
            else:
                monkey.throw(monkeys[monkey.if_false], worry_level)

monkey_business = list(map(lambda x: x.count, monkeys))
print(prod(sorted(monkey_business)[-2:]))
