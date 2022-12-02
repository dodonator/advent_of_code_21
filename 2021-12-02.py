# https://adventofcode.com/2021/day/2

# Dive! - Part One
from pathlib import Path

input_file = Path("2021-12-02_input.txt")

def part_one(input_file: Path):
    depth = 0
    position = 0
    with input_file.open("r") as file_obj:
        for line in file_obj:
            line = line.strip("\n")
            command, value = line.split(" ")
            value = int(value)
            
            if command == "forward":
                position += value
            elif command == "down":
                depth += value
            elif command == "up":
                depth -= value
    return depth * position

# Dive! - Part Two

def part_two(input_file: Path):
    depth = 0
    position = 0
    aim = 0
    with input_file.open("r") as file_obj:
        for line in file_obj:
            line = line.strip("\n")
            command, value = line.split(" ")
            value = int(value)
            
            if command == "forward":
                position += value
                depth += aim * value
            elif command == "down":
                aim += value
            elif command == "up":
                aim -= value
    return depth * position

print(part_two(input_file))
    

