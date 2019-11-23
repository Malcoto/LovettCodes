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
    return line

def parse_instructions(file_name):
    cleaned_line = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_line.append(parse_line(line))
    return cleaned_line

input = 'jlmsuwbz'
def validKey(hash, index):
    consecThreeCheck = False
    charKey = ''
    for charInd in range(len(hash) - 2):
        if hash[charInd] == hash[charInd + 1] and hash[charInd + 1] == hash[charInd + 2]:
            consecThreeCheck = True
            charKey = hash[charInd]
            break
    consecFiveCheck = False
    if consecThreeCheck:
        for i in range(1000):
            strInput = input + str(index + i + 1)
            futureHash = hashlib.md5(strInput.encode()).hexdigest()
            for charInd in range(len(futureHash) - 4):
                if futureHash[charInd] == charKey:
                    if futureHash[charInd] == futureHash[charInd + 1] and futureHash[charInd + 1] == futureHash[charInd + 2]:
                        if futureHash[charInd+2] == futureHash[charInd + 3] and futureHash[charInd + 3] == futureHash[charInd + 4]:
                            consecFiveCheck = True
    return consecThreeCheck and consecFiveCheck

def part_1():
    ind = 0

    key_count = 0
    while key_count < 64:
        strInput = input + str(ind)
        hash = hashlib.md5(strInput.encode()).hexdigest()
        isValid = validKey(hash, ind)
        if isValid:
            print(ind)
            key_count += 1
        ind +=1
    return ind - 1

def stretch_hash(strInput):
    new_hash = hashlib.md5(strInput.encode()).hexdigest()
    for i in range(2016):
        new_hash = hashlib.md5(new_hash.encode()).hexdigest()
    return new_hash

def stetch_validKey(hash, index, hashdict):
    consecThreeCheck = False
    charKey = ''
    for charInd in range(len(hash) - 2):
        if hash[charInd] == hash[charInd + 1] and hash[charInd + 1] == hash[charInd + 2]:
            consecThreeCheck = True
            charKey = hash[charInd]
            break
    consecFiveCheck = False

    if consecThreeCheck:
        for i in range(1000):
            strInput = input + str(index + i + 1)
            if hashdict[index + i + 1] == '':
                futureHash = stretch_hash(strInput)
                hashdict[index + i + 1] = futureHash
            else:
                futureHash = hashdict[index + i + 1]
            for charInd in range(len(futureHash) - 4):
                if futureHash[charInd] == charKey:
                    if futureHash[charInd] == futureHash[charInd + 1] and futureHash[charInd + 1] == futureHash[charInd + 2]:
                        if futureHash[charInd+2] == futureHash[charInd + 3] and futureHash[charInd + 3] == futureHash[charInd + 4]:
                            consecFiveCheck = True

    return consecThreeCheck and consecFiveCheck


def part_2():
    ind = 0

    hashes = defaultdict(str)

    key_count = 0
    while key_count < 64:
        strInput = input + str(ind)
        hash = stretch_hash(strInput)
        hashes[ind] = hash
        isValid = stetch_validKey(hash, ind, hashes)
        if isValid:
            print(ind)
            key_count += 1
        ind += 1
    return ind - 1


print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))


