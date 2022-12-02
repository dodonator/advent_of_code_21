# https://adventofcode.com/2021/day/12

from pathlib import Path

filename = f"input_" + Path(__file__).stem + ".txt"
filepath = Path(filename)

with filepath.open("r") as stream:
    pass
