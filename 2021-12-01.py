# https://adventofcode.com/2021/day/1

# Sonar Sweep - Part One
from pathlib import Path

input_file = Path("2021-12-01_input.txt")


def part_one(input_file: Path):
    with input_file.open("r") as file_obj:
        last_value = int(file_obj.readline().strip("\n"))

        increased = 0
        decreased = 0

        for line in file_obj:
            current_value = int(line.strip("\n"))

            if current_value > last_value:
                status = "increased"
                increased += 1

            elif current_value < last_value:
                status = "decreased"
                decreased += 1

            else:
                status = "equals"

            print(current_value, status)
            last_value = current_value

    return increased


# Sonar Sweep - Part Two
def part_two(input_file: Path):
    with input_file.open("r") as file_obj:
        last_window = [file_obj.readline() for i in range(3)]
        last_sum = sum(map(lambda line: int(line.strip("\n")), last_window))

        print(last_window, last_sum)

        inc_counter = 0
        while file_obj:
            next_line = file_obj.readline()
            if not next_line:
                break
            current_window = last_window[1:] + [next_line]
            current_sum = sum(map(lambda line: int(line.strip("\n")), current_window))

            if current_sum > last_sum:
                status = "increased"
                inc_counter += 1

            elif current_sum < last_sum:
                status = "decreased"

            else:
                status = "no change"

            print(current_window, current_sum, status)
            last_window = current_window
            last_sum = current_sum

    return inc_counter
