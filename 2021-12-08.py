# https://adventofcode.com/2021/day/8
from pathlib import Path
from collections import Counter


def get_translation(signal_pattern):
    remaining_pattern = list(signal_pattern)

    wire_table = {}
    translation_table = {}

    # rule 0 - finding one, four, seven and eight
    one_pattern = next(filter(lambda s: len(s) == 2, remaining_pattern))
    one = frozenset(one_pattern)
    remaining_pattern.remove(one_pattern)
    translation_table[one] = 1

    four_pattern = next(filter(lambda s: len(s) == 4, remaining_pattern))
    four = frozenset(four_pattern)
    remaining_pattern.remove(four_pattern)
    translation_table[four] = 4

    seven_pattern = next(filter(lambda s: len(s) == 3, remaining_pattern))
    seven = frozenset(seven_pattern)
    remaining_pattern.remove(seven_pattern)
    translation_table[seven] = 7

    eight_pattern = next(filter(lambda s: len(s) == 7, remaining_pattern))
    eight = frozenset(eight_pattern)
    remaining_pattern.remove(eight_pattern)
    translation_table[eight] = 8

    # rule 1 - combining one and seven
    wire_table["a"] = list(seven - one)[0]

    # rule 2 - finding two
    char1, char2 = one
    tmp_a = list(filter(lambda s: char1 in s and not char2 in s, remaining_pattern))
    tmp_b = list(filter(lambda s: char2 in s and not char1 in s, remaining_pattern))

    if len(tmp_a) == 1:
        two_pattern = tmp_a[0]
        wire_table["c"] = char1
        wire_table["f"] = char2
    elif len(tmp_b) == 1:
        two_pattern = tmp_b[0]
        wire_table["c"] = char2
        wire_table["f"] = char1

    two = frozenset(two_pattern)
    remaining_pattern.remove(two_pattern)
    translation_table[two] = 2

    # rule 3 - finding six
    for pattern in filter(lambda s: len(s) == 6, remaining_pattern):
        tmp_char = list(eight - frozenset(pattern))[0]
        if tmp_char in one:
            six_pattern = pattern
            six = frozenset(pattern)
            remaining_pattern.remove(six_pattern)
            translation_table[six] = 6

    # rule 4 - finding three and five
    pattern1, pattern2 = filter(lambda s: len(s) == 5, remaining_pattern)
    if wire_table["c"] in pattern1:
        pattern1, pattern2 = pattern2, pattern1

    five_pattern = pattern1
    five = frozenset(five_pattern)
    remaining_pattern.remove(five_pattern)
    translation_table[five] = 5

    three_pattern = pattern2
    three = frozenset(three_pattern)
    remaining_pattern.remove(three_pattern)
    translation_table[three] = 3

    wire_table["b"] = list(five - three)[0]
    wire_table["e"] = list(six - five)[0]

    # rule 5 - finding zero and nine
    pattern1, pattern2 = remaining_pattern
    if wire_table["e"] in pattern1:
        pattern1, pattern2 = pattern2, pattern1

    nine_pattern = pattern1
    nine = frozenset(nine_pattern)
    translation_table[nine] = 9

    zero_pattern = pattern2
    zero = frozenset(zero_pattern)
    translation_table[zero] = 0

    return translation_table


def decode(translation_table, output_values):
    digits = [translation_table[frozenset(v)] for v in output_values]
    return sum(d * 10**exp for exp, d in enumerate(reversed(digits)))


def part_one(input_file):
    with input_file.open("r") as file_obj:
        counter = 0
        for line in file_obj:
            line = line.strip("\n")
            signal_pattern, output_value = line.split("|")
            signal_pattern = [s for s in signal_pattern.split(" ") if s]
            output_value = [s for s in output_value.split(" ") if s]
            print(f"{signal_pattern},{output_value}")
            for digit in output_value:
                if len(digit) in (2, 3, 4, 7):
                    counter += 1
    return counter


def part_two(input_file):
    with input_file.open("r") as file_obj:
        result = 0
        for line in file_obj:
            line = line.strip("\n")
            signal_pattern, output_value = line.split("|")
            signal_pattern = [s for s in signal_pattern.split(" ") if s]
            output_value = [s for s in output_value.split(" ") if s]

            tt = get_translation(signal_pattern)
            current_value = decode(tt, output_value)
            result += current_value

    return result


input_file = Path("2021-12-08_input.txt")
