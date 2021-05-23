from random import random, shuffle, randint, sample, choice
from copy import deepcopy
from time import time
import sys

grid = []   # Holds rows of base grid
changeable = []   # Holds indices per row in 'grid' that are not fixed

"""
Processes a file and formulates a base grid, and keeps track of changeable indices.
Parameters
    file_path: Path to the file to be processed
"""


def process_file(file_path):

    with open(file_path, "r") as grid_file:
        grid_data = grid_file.readlines()

        for line in grid_data:
            current_row = []  # holds current row with empty spaces replaced with 0
            current_changeable = []  # hold indices of positions not fixed in a row
            index = 0

            # Ignore divider row.
            if line[0] == '-':
                continue

            for ch in line:
                # If number is not fixed, add a '0' placeholder & record index.
                if ch == '.':
                    current_row.append(0)
                    current_changeable.append(index)
                    index += 1

                elif ch != '\n' and ch != '!':
                    # If number is fixed, add to the base grid.
                    current_row.append(int(ch))
                    index += 1

            grid.append(current_row)
            changeable.append(current_changeable)
    print(changeable)
    print(grid)


process_file("grid1.txt")
