# https://adventofcode.com/2021/day/9
from pathlib import Path
from collections import namedtuple, Counter
from functools import reduce
from operator import mul

product = lambda iterable: reduce(mul, iterable)

Position = namedtuple("Position", ("x", "y"))
WIDTH, HEIGHT = 100, 100
input_file = Path("2021-12-09_input.txt")


def adjacent_positions(pos):
    x, y = pos
    if 0 < x:
        yield Position(x - 1, y)
    if x < WIDTH - 1:
        yield Position(x + 1, y)

    if 0 < y:
        yield Position(x, y - 1)
    if y < HEIGHT - 1:
        yield Position(x, y + 1)


def load_grid(input_file):
    with input_file.open("r") as file_obj:
        grid = dict()
        y_index = 0
        for line in file_obj:
            line = line.strip("\n")
            line = list(map(int, line))
            for x_index, value in enumerate(line):
                pos = Position(x_index, y_index)
                grid[pos] = value

            y_index += 1
    return grid


def part_one(input_file):
    grid = load_grid(input_file)
    risk_level = 0
    for position in grid:
        value = grid[position]
        adj_pos = adjacent_positions(position)
        adj_values = [grid[p] for p in adj_pos]
        low = all(map(lambda v: v > value, adj_values))
        if low:
            risk_level += value + 1
            print(position, risk_level)


grid = load_grid(input_file)
low_points = []
for position in grid:
    value = grid[position]
    adj_pos = adjacent_positions(position)
    adj_values = [grid[p] for p in adj_pos]
    low = all(map(lambda v: v > value, adj_values))
    if low:
        low_points.append(position)
for lp in low_points:
    print(lp)

basin_counter = Counter()
for lp in low_points:
    adj_pos = adjacent_positions(lp)
    pos_to_check = set(adj_pos)
    checked_pos = set()
    basin_size = 0
    while pos_to_check:
        new_pos = set()
        for pos in pos_to_check:
            checked_pos.add(pos)
            value = grid[pos]
            if value < 9:
                basin_size += 1
                adj_pos = set(adjacent_positions(pos))
                new_pos.update(adj_pos - checked_pos)
        pos_to_check = new_pos
    basin_counter[lp] = basin_size

largest_basins = dict(basin_counter.most_common(3))
largest_basins_values = largest_basins.values()
print(product(largest_basins_values))
