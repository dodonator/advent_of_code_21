# https://adventofcode.com/2021/day/6
from pathlib import Path
from collections import Counter


def part_one(input_file):
    with input_file.open("r") as file_obj:
        content = file_obj.read()
        data = list(map(int, content.strip("\n").split(",")))

    old_state = list(data)
    new_state = []
    for iteration in range(80):
        create_counter = 0
        for i, timer in enumerate(old_state):
            if timer == 0:
                new_state.append(6)
                create_counter += 1
            else:
                new_state.append(timer - 1)
        for c in range(create_counter):
            new_state.append(8)
        print(iteration, len(new_state))
        old_state = list(new_state)
        new_state = list()
    return len(old_state)


def part_two(input_file):
    with input_file.open("r") as file_obj:
        content = file_obj.read()
        data = list(map(int, content.strip("\n").split(",")))

    old_state = Counter(data)
    for iteration in range(256):
        new_state = Counter()
        for timer, count in old_state.items():
            if timer == 0:
                new_state[8] = count
                new_state[6] = new_state.get(6, 0) + count
            elif timer == 7:
                new_state[6] = new_state.get(6, 0) + count
            else:
                new_state[timer - 1] = count
        print(iteration, new_state)
        old_state = Counter(new_state)
    return sum(old_state.values())


input_file = Path("2021-12-06_input.txt")
print(part_two(input_file))
