import collections
import re
import math
import time
import numpy as np
import sys
import os
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
import utils


## TODO Change file path to appropriate input file.
INPUT_FILE_NAME = "Inputs/day_X_input"

## TODO Implement per line interpretation of input (If applicable)
def parse_line(line):
    return line

def parse_instructions(file_name):
    cleaned_line = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_line.append(parse_line(line))
    return cleaned_line

## TODO Implement part 1 solution
def part_1():
    pass

## TODO Implement part 2 solution
def part_2():
    pass


print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))


