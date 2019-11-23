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
INPUT_FILE_NAME = "Inputs/Day4part1"

## TODO Implement per line interpretation of input (If applicable)
def parse_line(line):
    cleaned_line=[]
    for word in line.strip("\n").split(" "):
        cleaned_line.append(word)
    return cleaned_line

def parse_instructions(file_name):
    cleaned_lines = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_lines.append(parse_line(line))
    return cleaned_lines


## TODO Implement part 1 solution

def part_1():
    passphrases=parse_instructions(INPUT_FILE_NAME)
    print passphrases
    print len(passphrases)
    valid=0
    for passphrase in passphrases:
        words_used=collections.defaultdict(int)
        failed=0
        for word in passphrase:
            if words_used[word]==1:
                failed=1
                break
            else:
                words_used[word]=1
        if failed==0:
            valid+=1
    return valid

## TODO Implement part 2 solution
def part_2():
    passphrases = parse_instructions(INPUT_FILE_NAME)
    valid = 0
    for passphrase in passphrases:
        words_used = collections.defaultdict(int)
        failed = 0
        for word in passphrase:
            if words_used[tuple(sorted(word))] == 1:
                failed = 1
                break
            else:
                words_used[tuple(sorted(word))] = 1
        if failed == 0:
            valid += 1
    return valid



print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))


