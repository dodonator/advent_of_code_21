# https://adventofcode.com/2021/day/5
from pathlib import Path
from collections import namedtuple, Counter
from itertools import chain


def flatten(list_of_lists):
    "Flatten one level of nesting"
    return chain.from_iterable(list_of_lists)


Position = namedtuple("Position", ("x", "y"))


def part_one(input_file):
    lines = []
    with input_file.open("r") as file_obj:
        for line in file_obj:
            pos1, pos2 = line.strip("\n").split(" -> ")
            pos1 = Position(*list(map(int, pos1.split(","))))
            pos2 = Position(*list(map(int, pos2.split(","))))
            lines.append((pos1, pos2))

    full_lines = []

    for pos1, pos2 in lines:
        x1, y1 = pos1
        x2, y2 = pos2
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1

            line = []
            for y in range(y1, y2 + 1):
                pos = Position(x1, y)
                line.append(pos)
            full_lines.append(line)

        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1

            line = []
            for x in range(x1, x2 + 1):
                pos = Position(x, y1)
                line.append(pos)
            full_lines.append(line)

    counter = Counter(flatten(full_lines))
    result = len([pos for pos, value in counter.items() if value > 1])
    return result


def part_two(input_file):
    lines = []
    with input_file.open("r") as file_obj:
        for line in file_obj:
            pos1, pos2 = line.strip("\n").split(" -> ")
            pos1 = Position(*list(map(int, pos1.split(","))))
            pos2 = Position(*list(map(int, pos2.split(","))))
            lines.append((pos1, pos2))

    full_lines = []
    for pos1, pos2 in lines:
        x1, y1 = pos1
        x2, y2 = pos2
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1

            line = []
            for y in range(y1, y2 + 1):
                pos = Position(x1, y)
                line.append(pos)
                
            full_lines.append(line)
            print(line)
        
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1

            line = []
            for x in range(x1, x2 + 1):
                pos = Position(x, y1)
                line.append(pos)
            full_lines.append(line)
            print(line)
        
        else:
            step_x = -1 if x1 > x2 else 1
            step_y = -1 if y1 > y2 else 1
            range_x = range(x1, x2+step_x, step_x)
            range_y = range(y1, y2+step_y, step_y)
            
            line = []
            for x, y in zip(range_x, range_y):
                pos = Position(x,y)
                line.append(pos)
            print(line)
            full_lines.append(line)
    
    counter = Counter(flatten(full_lines))
    result = len([pos for pos, value in counter.items() if value > 1])
    return result

input_file = Path("2021-12-05_input.txt")
print(part_two(input_file))
