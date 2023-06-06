PUZZLE_INPUT_PATH = "./inputs/1.txt"
TEST_INPUT_PATH = "./inputs/1-test.txt"


def get_puzzle_input(file_path: str = PUZZLE_INPUT_PATH) -> list:

    with open(file_path) as input:
        return map(lambda x: int(x.rstrip('\n')), input.readlines())


def sum_to_2020(nums: list) -> tuple:
    """Returns two numbers in input that sum to 2020."""
    l = len(nums)

    for i in range(l):
        num1 = nums[i]

        for j in range(l):
            if i == j:
                continue
            num2 = nums[j]

            if num1 + num2 == 2020:
                return num1, num2
            

def sum_to_2020_2(nums: list) -> tuple:
    """Return three numbers in input that sum to 2020"""
    l = len(nums)

    for i in range(l):
        num1 = nums[i]

        for j in range(l):
            if i == j:
                continue
            num2 = nums[j]

            for k in range(l):
                if k == i or k == j:
                    continue
                num3 = nums[k]

                if num1 + num2 + num3 == 2020:
                    return num1, num2, num3



if __name__ == "__main__":

    nums = list(get_puzzle_input())

    part1_nums = sum_to_2020(nums)
    part1_result = part1_nums[0] * part1_nums[1]

    print("======= PART 1 =======")
    print(part1_result)

    part2_nums = sum_to_2020_2(nums)
    part2_result = part2_nums[0] * part2_nums[1] * part2_nums[2]

    print("======= PART 2 =======")
    print(part2_result)
    
    