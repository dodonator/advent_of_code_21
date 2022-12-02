# https://adventofcode.com/2021/day/10
from advent_of_code import get_input_data
from statistics import median

input_file = get_input_data(2021, 10)

# corrupted lines
def part_one():
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

    bracket_types = ("(", "[", "{", "<", ")", "]", "}", ">")

    with input_file.open("r") as file_obj:
        error_sum = 0
        for line in file_obj:
            line = line.strip("\n")
            stack = list()
            for char in line:
                entry = bracket_types.index(char)

                if entry < 4:
                    stack.append(entry)
                else:
                    last = stack.pop()
                    expected = bracket_types[last + 4]
                    if expected != char:
                        error = scores.get(char)
                        error_sum += error
                        continue

    return error_sum


# incomplete lines
def part_two():
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    bracket_types = ("(", "[", "{", "<", ")", "]", "}", ">")
    line_scores = []
    with input_file.open("r") as file_obj:
        for line in file_obj:
            line = line.strip("\n")
            complete = complete_line(line)
            if complete is None:
                continue

            remainder = complete[len(line) :]
            score = 0
            for char in remainder:
                score = score * 5
                score = score + scores[char]
            print(remainder, score)
            line_scores.append(score)
    return median(line_scores)


def complete_line(line):
    bracket_types = ("(", "[", "{", "<", ")", "]", "}", ">")
    stack = list()
    for char in line:
        entry = bracket_types.index(char)

        if entry < 4:
            stack.append(entry)
        else:
            last = stack.pop()
            expected = bracket_types[last + 4]
            if expected != char:
                return None
    line_score = 0
    while stack:
        last = stack.pop()
        expected = bracket_types[last + 4]
        line += expected
    return line


print(part_two())
