# https://adventofcode.com/2021/day/3
from pathlib import Path
from collections import Counter

input_file = Path("2021-12-03_input.txt")

# Binary Diagnostic - Part One
def part_one(input_file: Path):
    with input_file.open("r") as file_obj:
        bit_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for line in file_obj:

            line = line.strip("\n")
            print(line)
            for i in range(12):
                if int(line[i]):
                    bit_counter[i] += 1
                else:
                    bit_counter[i] -= 1
        gamma_rate_bits = [int(b > 0) for b in bit_counter]
        epsilon_rate_bits = [int(not b) for b in gamma_rate_bits]

        print(12 * "-")
        gamma_rate = int("".join(map(str, gamma_rate_bits)), base=2)
        epsilon_rate = int("".join(map(str, epsilon_rate_bits)), base=2)

        return gamma_rate * epsilon_rate


with input_file.open("r") as file_obj:
    data = list()
    for line in file_obj:
        line = line.strip("\n")
        data.append(line)

# oxygen
oxygen_data = list(data)
i = 0
while len(oxygen_data) > 1:
    bits = [d[i] for d in oxygen_data]
    counter = Counter(bits)

    most_common = counter.most_common()[0][0]
    if counter["0"] == counter["1"]:
        most_common = "1"

    oxygen_data = list(filter(lambda e: e[i] == most_common, oxygen_data))
    # print(oxygen_data)
    i += 1

oxygen_rating = int(oxygen_data[0], base=2)
print(f"{oxygen_rating=}")

# co2
co2_data = list(data)
i = 0
while len(co2_data) > 1:
    bits = [d[i] for d in co2_data]
    counter = Counter(bits)

    least_common = counter.most_common()[1][0]
    if counter["0"] == counter["1"]:
        least_common = "0"

    co2_data = list(filter(lambda e: e[i] == least_common, co2_data))
    # print(co2_data)
    i += 1

co2_rating = int(co2_data[0], base=2)
print(f"{co2_rating=}")

print(oxygen_rating * co2_rating)
