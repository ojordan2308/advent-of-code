from io import StringIO


INPUT_PATH = './input.txt'
TEST_INPUT_PATH = './test-input.txt'
PAIR_INSERTION = {}
EXTRAS = {}


def get_template_and_pairs(puzzle_input_path = INPUT_PATH,
                           pair_insertion_dict = PAIR_INSERTION):
    with open(puzzle_input_path) as input:
        for line in input:
            line = line.rstrip('\n')
            if '->' in line:
                pair, insert = tuple(map(lambda x: x.strip(), line.split('->')))
                pair_insertion_dict[pair] = insert
            elif line:
                template = line
    return template


def get_template_and_pairs_2(puzzle_input_path = INPUT_PATH,
                             pair_insertion_dict = PAIR_INSERTION,
                             extras = EXTRAS):
    with open(puzzle_input_path) as input:
        for line in input:
            line = line.rstrip('\n')
            if '->' in line:
                pair, insert = tuple(map(lambda x: x.strip(), line.split('->')))
                pair_insertion_dict[pair] = insert
            elif line:
                for letter in line[1:-1]:
                    if letter in extras:
                        extras[letter] += 1
                    else:
                        extras[letter] = 1
                template = {}
                for i in range(len(line)-1):
                    pair = line[i] + line[i+1]
                    if pair in template:
                        template[pair] += 1
                    else:
                        template[pair] = 1
    return template


def insert(template, pair_insertion_dict = PAIR_INSERTION):
    result = ''
    for i in range(len(template)-1):
        pair = template[i] + template[i+1]
        if pair:
            result += f'{pair[0]}{pair_insertion_dict[pair]}'
    result += template[-1]
    return result


def insert_2(template, pair_insertion_dict = PAIR_INSERTION):
    result = StringIO()
    for i in range(len(template)-1):
        pair = template[i] + template[i+1]
        if pair:
            result.write(f'{pair[0]}{pair_insertion_dict[pair]}')
    result.write(template[-1])
    return result.getvalue()


def insert_3(template_dict, pair_insertion_dict = PAIR_INSERTION, extras = EXTRAS):
    new_template_dict = {}
    for pair in template_dict:
        n = template_dict[pair]
        insert = pair_insertion_dict[pair]

        if insert in extras:
            extras[insert] += n
        else:
            extras[insert] = n

        new_pair_1 = pair[0] + insert
        new_pair_2 = insert + pair[1]

        if new_pair_1 in new_template_dict:
            new_template_dict[new_pair_1] += n
        else:
            new_template_dict[new_pair_1] = n

        if new_pair_2 in new_template_dict:
            new_template_dict[new_pair_2] += n
        else:
            new_template_dict[new_pair_2] = n
    return new_template_dict


def get_letter_frequency_range(template):
    letter_frequencies = {}
    for letter in template:
        if letter in letter_frequencies:
            letter_frequencies[letter] += 1
        else:
            letter_frequencies[letter] = 1
    max_frequency = max(letter_frequencies.values())
    min_frequency = min(letter_frequencies.values())
    return max_frequency - min_frequency


def get_letter_frequency_range_2(template_dict, extras = EXTRAS):
    letter_frequencies = {}
    for pair in template_dict:
        n = template_dict[pair]
        for letter in pair:
            if letter in letter_frequencies:
                letter_frequencies[letter] += n
            else:
                letter_frequencies[letter] = n
    for letter in extras:
        letter_frequencies[letter] -= extras[letter]
    max_frequency = max(letter_frequencies.values())
    min_frequency = min(letter_frequencies.values())
    return max_frequency - min_frequency


if __name__ == "__main__":
    
    polymer_template_dict = get_template_and_pairs_2()

    for i in range(40):
        polymer_template_dict = insert_3(polymer_template_dict)
        if i == 9:
            print("========Part1========")
            print(get_letter_frequency_range_2(polymer_template_dict))
    print("========Part2========")
    print(get_letter_frequency_range_2(polymer_template_dict))
