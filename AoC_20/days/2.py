import re


PUZZLE_INPUT_PATH = "./inputs/2.txt"
TEST_INPUT_PATH = "./inputs/2-test.txt"


def get_puzzle_input(input_path: str = PUZZLE_INPUT_PATH) -> list[dict]:
    parsed_input = []
    with open(input_path) as input:
        for line in input:
            line = line.rstrip('\n')

            password = {}
            password["range"] = tuple(map(lambda x: int(x),
                                          re.search("\d+-\d+", line).group(0).split("-")))
            password["letter"] = re.search(".(?=:)", line).group(0)
            password["password"] = re.search("(?<=: ).*", line).group(0)

            parsed_input.append(password)
    return parsed_input


def find_valid_passwords(passwords: list[dict]) -> int:
    count = 0

    for p in passwords:
        password = p["password"]
        min, max = p["range"]
        letter = p["letter"]

        n = password.count(letter)
        if n >= min and n <= max:
            count += 1

    return count


def find_valid_passwords_2(passwords: list[dict]) -> int:
    count = 0

    for p in passwords:
        password = p["password"]
        i, j = p["range"]
        letter = p["letter"]

        if bool(password[i-1]==letter) != bool(password[j-1]==letter):
            count += 1

    return count




if __name__ == "__main__":
    
    input = get_puzzle_input()
    part1_result = find_valid_passwords(input)
    part2_result = find_valid_passwords_2(input)

    print("======= PART 1 =======")
    print(part1_result)

    print("======= PART 2 =======")
    print(part2_result)
