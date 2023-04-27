INPUT_PATH = './input.txt'
TEST_INPUT_PATH = './test-input.txt'
CAVES = []
PATHS = []

class Cave:
    def __init__(self, name, is_big, is_start, is_end):
        self.name = name
        self.connects = []
        self.is_big = is_big
        self.is_start = is_start
        self.is_end = is_end

    def __repr__(self):
        return self.name
    
    @classmethod
    def get_caves(self, puzzle_input_path = INPUT_PATH, caves = CAVES):
        with open(puzzle_input_path) as input:
            cave_links = map(lambda x: x.split('-'),
                            map(lambda x: x.rstrip('\n'), input.readlines()))

        for link in cave_links:
            for cave_name in link:
                if cave_name not in map(lambda x: x.name, caves):
                    real_cave = Cave(name = cave_name,
                                    is_big = cave_name.upper()==cave_name,
                                    is_start = cave_name=='start',
                                    is_end = cave_name=='end')
                    caves.append(real_cave)

            cave_1 = list(filter(lambda x: x.name == link[0], caves))[0]
            cave_2 = list(filter(lambda x: x.name == link[1], caves))[0]
            cave_1.connects.append(cave_2)
            cave_2.connects.append(cave_1)


class Path:
    def __init__(self, caves_visited):
        self.caves_visited = caves_visited

    def fork(self, next_caves, paths):
        paths += [Path([*[c for c in self.caves_visited], cave])
                  for cave in next_caves]


if __name__ == "__main__":
    
    Cave.get_caves()
    start_cave = list(filter(lambda x: x.is_start, CAVES))[0]
    end_cave = list(filter(lambda x: x.is_end, CAVES))[0]
    small_caves = list(filter(lambda x: not x.is_big and x.name not in ('start', 'end'), CAVES))
    end_cave.connects = []

    current_caves = [start_cave]
    PATHS += [Path([start_cave])]
    while current_caves:
        current_caves = []
        forked_paths = []
        for path in PATHS:

            #PART 1 next_caves = [cave for cave in path.caves_visited[-1].connects
            # if not (not cave.is_big and cave in path.caves_visited)]
            if list(filter(lambda x: x in small_caves and path.caves_visited.count(x) == 2,
                           path.caves_visited)):
                next_caves = [cave for cave in path.caves_visited[-1].connects
                              if not (not cave.is_big and cave in path.caves_visited)]
            else:
                next_caves = [cave for cave in path.caves_visited[-1].connects
                              if not cave.name == 'start']

            if not next_caves:
                forked_paths.append(path)
                continue

            current_caves += next_caves
            path.fork(next_caves, forked_paths)

        PATHS = forked_paths
        
    print(len(list(filter(lambda x: x.caves_visited[-1] == end_cave, PATHS))))
