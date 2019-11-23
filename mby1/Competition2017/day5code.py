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
INPUT_FILE_NAME = "Inputs/day5"

## TODO Implement per line interpretation of input (If applicable)
def parse_line(line):
    return line

def parse_instructions(file_name):
    cleaned_line = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_line.append(int(parse_line(line)))
    return cleaned_line


## TODO Implement part 1 solution
def part_1():
    instructions=parse_instructions(INPUT_FILE_NAME)
    current=0
    steps=0
    while current <= len(instructions)-1 and current >=0:
        steps+=1
        instructions[current]+=1
        current+=instructions[current]-1
    return steps



## TODO Implement part 2 solution
def part_2():
    instructions=parse_instructions(INPUT_FILE_NAME)
    current=0
    steps=0
    while current <= len(instructions)-1 and current >=0:
        steps+=1
        if instructions[current]>=3:
            instructions[current]-=1
            current+=instructions[current]+1
        else:
            instructions[current]+=1
            current+=instructions[current]-1
    return steps


print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))


