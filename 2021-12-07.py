# https://adventofcode.com/2021/day/7
from pathlib import Path
from statistics import median, mean


def read_data(input_file):
    with input_file.open("r") as file_obj:
        content = file_obj.read()
        data = list(map(int, content.strip("\n").split(",")))
    return data


def cost(origin, target):
    return sum(range(abs(origin - target) + 1))


def total_cost(data, value):
    result = 0
    for d in data:
        current_cost = cost(d, value)
        result += current_cost
    return result


def part_one(input_file):
    data = read_data(input_file)

    data_median = median(data)
    return sum(abs(d - data_median) for d in data)


def part_two(input_file):
    data = read_data(input_file)

    start_value = round(mean(data))
    current_value = start_value
    current_total = total_cost(data, current_value)

    running = True
    while running:
        new_value_a = current_value + 1
        new_value_b = current_value - 1

        new_total_a = total_cost(data, new_value_a)
        new_total_b = total_cost(data, new_value_b)

        print(f"{new_value_a:>8} -> {new_total_a}")
        print(f"{new_value_b:>8} -> {new_total_b}")

        if new_total_a < current_total:
            current_value = new_value_a
            current_total = new_total_a

        elif new_total_b < current_total:
            current_value = new_value_b
            current_total = new_total_b

        else:
            break

    return current_total


input_file = Path("2021-12-07_input.txt")
