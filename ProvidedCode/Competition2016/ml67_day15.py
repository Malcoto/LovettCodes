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
from collections import defaultdict
import hashlib

INPUT_FILE_NAME = "Inputs/input.txt"

def parse_line(line):
    strings = line.split(" ")
    discnum = int(strings[1][1:])
    position = int(strings[-1].strip("\n").strip("."))
    slotAvailable = int(strings[3])
    return (discnum, position, slotAvailable)

def parse_instructions(file_name):
    cleaned_line = defaultdict(tuple)
    with open(file_name) as input_file:
        for line in input_file.readlines():
            (discnum, position, slotAvailable) = parse_line(line)
            cleaned_line[discnum] = (position, slotAvailable)
    return cleaned_line

def part_1():
    discToPos = parse_instructions(INPUT_FILE_NAME)
    print (discToPos)
    num_disc = len(discToPos)
    passing = False
    time_start = 0
    while not passing:
        passing = True
        # print (time_start)
        for disc in range(1, num_disc + 1):
            # print('time', time_start)
            # print((discToPos[disc][0] + disc + time_start) % discToPos[disc][1])
            # print("disc", disc)
            if (discToPos[disc][0] + disc + time_start) % discToPos[disc][1] != 0:

                passing = False
                break
        if passing:
            break
        time_start +=1

    return time_start
def part_2():
    #literally part 1 with different inputs
    pass


print("Part 1 answer: {}".format(part_1()))


