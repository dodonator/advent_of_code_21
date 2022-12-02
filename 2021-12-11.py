# https://adventofcode.com/2021/day/11
from util import get_input_data
from collections import namedtuple
from itertools import product


def load_data(input_file):
    with input_file.open("r") as file_obj:
        data = list()
        for line in file_obj:
            line = line.strip("\n")
            line_data = list(map(int, line))
            data.append(line_data)
    return data


def gen_grid(data):
    grid = dict()
    for y, row in enumerate(data):
        for x, value in enumerate(row):
            pos = Position(x, y)
            grid[pos] = value
    return grid


def adjacent(pos):
    x, y = pos
    candidates = [(x + o[0], y + o[1]) for o in offsets]
    positions = [(x, y) for x, y in candidates if 0 <= x < WIDTH and 0 <= y < HEIGHT]
    return [Position(x, y) for x, y in positions]


def adjacent_positions():
    adj = dict()
    for pos in positions:
        adj[pos] = adjacent(pos)
    return adj


def print_grid(grid):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            pos = Position(x, y)
            print(f"{grid[pos]} ", end="")
        print()
    print()


def step(grid):
    for pos in grid:
        grid[pos] += 1
    to_flash = list(filter(lambda pos: grid[pos] > 9, grid))
    flashed = set()
    flash_counter = 0
    while to_flash:
        for pos in to_flash:
            grid[pos] = 0
            flashed.add(pos)
            for adj in adjacent_positions[pos]:
                grid[adj] += 1
            flash_counter += 1
        to_flash = list(filter(lambda pos: grid[pos] > 9, grid))
    for pos in flashed:
        grid[pos] = 0
    return grid, flash_counter


Position = namedtuple("Position", ("x", "y"))
input_file = get_input_data(2021, 11)
WIDTH, HEIGHT = 10, 10

offsets = list(product((-1, 0, 1), (-1, 0, 1)))
offsets.remove((0, 0))

positions = [Position(x, y) for x, y in product(range(WIDTH), range(HEIGHT))]
adjacent_positions = {pos: adjacent(pos) for pos in positions}


def part_one():
    data = load_data(input_file)
    grid = gen_grid(data)

    flash_counter = 0
    for i in range(100):
        grid, counter = step(grid)
        flash_counter += counter
    return flash_counter


def part_two():
    data = load_data(input_file)
    grid = gen_grid(data)
    flash_counter = 0
    step_counter = 0
    while flash_counter < 100:
        grid, flash_counter = step(grid)
        step_counter += 1
    return step_counter
