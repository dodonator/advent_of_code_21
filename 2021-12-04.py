# https://adventofcode.com/2021/day/4
from pathlib import Path
from collections import namedtuple

Position = namedtuple("Position", ("x", "y"))


class Grid:
    def __init__(self, grid_lines):
        self.cells = dict()

        for x, line in enumerate(grid_lines):
            for y, number in enumerate(line):
                pos = Position(x, y)
                self.cells[pos] = [number, False]

    def check(self):
        rows = [
            [self.cells.get(Position(x, y))[1] for y in range(5)] for x in range(5)
        ]
        columns = [
            [self.cells.get(Position(x, y))[1] for x in range(5)] for y in range(5)
        ]
        
        return any((all(r) for r in rows)) or any((all(c) for c in columns))

    def update(self, number):
        for x in range(5):
            for y in range(5):
                pos = Position(x,y)
                if self.cells.get(pos)[0] == number:
                    self.cells.get(pos)[1] = True
    
    def unmarked(self):
        for x in range(5):
            for y in range(5):
                pos = Position(x,y)
                if not self.cells.get(pos)[1]:
                    yield self.cells.get(pos)[0]
                    

def part_one(input_file):
    with input_file.open("r") as file_obj:
        first_line = file_obj.readline()
        numbers = [int(n) for n in first_line.strip("\n").split(",")]

        grid_list = list()

        counter = 0
        while file_obj.readline():
            grid_lines = []
            for i in range(5):
                line = file_obj.readline().strip("\n")
                row = list(map(int, filter(bool, line.split(" "))))
                grid_lines.append(row)

            current_grid = Grid(grid_lines)
            grid_list.append(current_grid)

    running = True
    numbers = iter(numbers)

    while running:
        number = next(numbers)
        print(number)
        for g_id, grid in enumerate(grid_list):
            grid.update(number)
            status = grid.check()
            if status:
                print(number, g_id)
                winning_board = grid
                winning_number = number
                
                running = False
                break
            
    sum_of_unmarked = sum(winning_board.unmarked())
    result = sum_of_unmarked * winning_number
    return result


def part_two(input_file):
    with input_file.open("r") as file_obj:
        first_line = file_obj.readline()
        numbers = [int(n) for n in first_line.strip("\n").split(",")]

        grid_list = list()

        counter = 0
        while file_obj.readline():
            grid_lines = []
            for i in range(5):
                line = file_obj.readline().strip("\n")
                row = list(map(int, filter(bool, line.split(" "))))
                grid_lines.append(row)

            current_grid = Grid(grid_lines)
            grid_list.append(current_grid)

    board_stati = dict(enumerate(len(grid_list)*[False]))
    print(board_stati)
    
    for number in numbers:
        for b_id, board in enumerate(grid_list):
            if not board_stati[b_id]:
                board.update(number)
                new_status = board.check()
                if new_status:
                    board_stati[b_id] = True
                    
                    sum_of_unmarked = sum(board.unmarked())
                    result = sum_of_unmarked * number
                    
                    print(b_id, number, result)
    
input_file = Path("2021-12-04_input.txt")
print(part_two(input_file))