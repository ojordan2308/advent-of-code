class LanternFish:
    def __init__(self, timer):
        self.timer = timer

    def __repr__(self):
        return str(self.timer)

    def age(self, lantern_fishes):
        if self.timer == 0:
            lantern_fishes.append(LanternFish(8))
            self.timer = 6
        else:
            self.timer -= 1

def how_many_fish(timer, days):
    total_fish = 1
    days_remaining = days - timer - 1
    if days_remaining < 0:
        return total_fish
    total_fish += how_many_fish(8, days_remaining)
    while days_remaining >= 7:
        days_remaining -= 7
        total_fish += how_many_fish(8, days_remaining)
    return total_fish



if __name__ == "__main__":
    with open('./input.txt') as input:
        for line in input:
            LANTERN_FISH = list(map(lambda x: LanternFish(int(x)),
                                    line.split(',')))
            TIMERS = list(map(lambda x: int(x),
                              line.split(',')))
    
    DAYS = 256

    total = 0
    for timer in set(TIMERS):
        count = TIMERS.count(timer)
        total += how_many_fish(timer, DAYS) * count
    print(total)

    """part2_result = 0
    for timer in range(1,6):
        lantern_fishes = [LanternFish(timer)]
        for day in range(256):
            for i in range(len(lantern_fishes)):
                fish = lantern_fishes[i]
                fish.age(lantern_fishes)
        part2_result += len(lantern_fishes) * TIMERS_COUNTS[timer]
    print(part2_result)"""

    """for day in range(80):
        for i in range(len(LANTERN_FISH)):
            fish = LANTERN_FISH[i]
            fish.age(LANTERN_FISH)
    
    print(len(LANTERN_FISH))"""