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

INPUT_FILE_NAME = "Inputs/input.txt"

def parse_line(line):
    return line

def parse_instructions(file_name):
    cleaned_line = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_line.append(parse_line(line))
    return cleaned_line

def isOb(node):
    x = node[0]
    y = node[1]
    num = x*x + 3*x + 2*x*y + y + y*y
    fav_num = 1350
    summ = str(bin(num + fav_num))[2:]
    actual_summ = 0
    for char in summ:
        actual_summ += int(char)
    return False if actual_summ % 2 == 0 else True

def neighbor(node):
    viable_nbr = []
    # node in format (0:x, 1:y)
    x = node[0]
    y = node[1]
    viable_nbr.append((x+1,y))
    viable_nbr.append((x, y+1))
    if x != 0:
        viable_nbr.append((x-1, y))
    if y != 0:
        viable_nbr.append((x, y - 1))
    return viable_nbr

def part_1():
    visited = []
    dist = defaultdict(int)
    start = (1,1)
    goal = (31,39)
    queue = []
    queue.insert(0,start)
    while len(queue) != 0:
        cur = queue.pop()
        for nbr in neighbor(cur):
            if (not isOb(nbr)) and (nbr not in visited):
                dist[nbr] = dist[cur] + 1
                visited.append(nbr)
                queue.insert(0,nbr)
            if nbr[0] == goal[0] and nbr[1] == goal[1]:

                return dist[nbr]


## TODO Implement part 2 solution
def part_2():
    visited = []
    dist = defaultdict(int)
    start = (1, 1)
    queue = []
    queue.insert(0, start)
    reachable = set()
    while len(queue) != 0:
        cur = queue.pop()
        for nbr in neighbor(cur):
            if (not isOb(nbr)) and (nbr not in visited):
                dist[nbr] = dist[cur] + 1

                queue.insert(0, nbr)
                visited.append(nbr)
                if dist[nbr] <= 50:
                    reachable.add(nbr)
            halt = False
            for key, val in dist.items():

                if val > 50:
                    halt = True
            if halt:
                return len(reachable)

print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))


