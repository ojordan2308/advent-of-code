from itertools import permutations
import json
import queue


INPUT_PATH = './input.txt'
TEST_INPUT_PATH = './test-input.txt'


class Pair:

    def __init__(self, left, right, previous):
        if isinstance(left, list):
            self.left = Pair(left[0], left[1], self)
        else:
            self.left = left

        if isinstance(right, list):
            self.right = Pair(right[0], right[1], self)
        else:
            self.right = right
        
        self.previous = previous


    def __repr__(self):
        return f"[{self.left}, {self.right}]"
    

    def explode(self, pair):
        # check for closest number to the left
        current = pair
        while current and current.previous and current != self:
            if current != current.previous.left:
                searching = True
                search = current.previous
                if isinstance(search.left, int):
                    search.left += pair.left
                    searching = False
                else:
                    search = search.left
                while searching:
                    if isinstance(search.right, int):
                        search.right += pair.left
                        searching = False
                    else:
                        search = search.right
                break
            current = current.previous
        # check for closest number to the right
        current = pair
        while current and current.previous and current != self:
            if current != current.previous.right:
                searching = True
                search = current.previous
                if isinstance(search.right, int):
                    search.right += pair.right
                    searching = False
                else:
                    search = search.right
                while searching:
                    if isinstance(search.left, int):
                        search.left += pair.right
                        searching = False
                    else:
                        search = search.left
                break
            current = current.previous
        # replace exploded pair with 0
        if pair.previous.right == pair:
            pair.previous.right = 0
        elif pair.previous.left == pair:
            pair.previous.left = 0

    
    def explode_deepest_pair(self):
        current = None
        q = queue.Queue()
        q.put(self)

        pair_depth = {}

        while not q.empty():
            current = q.get()
            if isinstance(current.left, Pair):
                q.put(current.left)
            if isinstance(current.right, Pair):
                q.put(current.right)

            level = 0
            up = current
            while up and up != self:
                up = up.previous
                level += 1
            pair_depth[current] = level

        deepest_pair = max(pair_depth, key=pair_depth.get)
        if pair_depth[deepest_pair] >= 4:
            self.explode(deepest_pair)
            self.explode_deepest_pair()

    
    def split(self, root):
        if isinstance(self.left, Pair):
            self.left.split(root)
        elif isinstance(self.left, int):
            num = self.left
            if num > 9:
                self.left = Pair(num//2, num - num//2, self)
                root.explode_deepest_pair()
                root.split(root)
        if isinstance(self.right, Pair):
            self.right.split(root)
        elif isinstance(self.right, int):
            num = self.right
            if num > 9:
                self.right = Pair(num//2, num - num//2, self)
                root.explode_deepest_pair()
                root.split(root)


    def add(self, pair):
        new_pair = Pair(self, pair, None)
        self.previous = new_pair
        pair.previous = new_pair
        return new_pair
    

    def magnitude(self):
        total = 0
        if isinstance(self.left, int):
            total += 3*self.left
        else:
            total += 3*self.left.magnitude()
        if isinstance(self.right, int):
            total += 2*self.right
        else:
            total += 2*self.right.magnitude()
        return total


    @classmethod
    def get_input(self, puzzle_input_path = INPUT_PATH):
        with open(puzzle_input_path) as input:
            summands = list(map(lambda x: json.loads(x.rstrip("\n")), input.readlines()))

        return [Pair(left=s[0], right=s[1], previous=None) for s in summands]


    @classmethod
    def get_input2(self, puzzle_input_path = INPUT_PATH):
        with open(puzzle_input_path) as input:
            summands = list(map(lambda x: json.loads(x.rstrip("\n")), input.readlines()))

        return permutations(summands, 2)


if __name__ == "__main__":

    fish_numbers = Pair.get_input()
    addition_result = fish_numbers[0]

    for num in fish_numbers[1:]:
        addition_result = addition_result.add(num)
        addition_result.explode_deepest_pair()
        addition_result.split(root=addition_result)

    print("======PART 1======")
    print(addition_result.magnitude())

    fish_numbers = Pair.get_input2()
    magnitudes = {}
    for comb in fish_numbers:
        num = Pair(comb[0], comb[1], None)
        num.explode_deepest_pair()
        num.split(root=num)
        magnitudes[num] = num.magnitude()
    
    print("======PART 2======")
    max_magnitude = max(magnitudes, key=magnitudes.get)
    print(magnitudes[max_magnitude])

