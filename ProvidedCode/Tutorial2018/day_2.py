# TODO Read through the day 1 problem of 2018, then you can go through this file and try to implement the given
# suggestions to make the code work! (Delete all TODOs when finished.)


## TODO Change file path to appropriate input file.
INPUT_FILE_NAME = "Inputs/dayXInput.txt"


## TODO" First we will write a function that can process the character inputs line
# by line. We will cast these strings to an integer by calling int(line).
def parse_line(line):
    # The variable line is of type string. This makes it difficult to add together, so
    # we will cast the line to an integer, so that they can be added together.

    ## TODO: Uncomment, then complete the line below.
    integer = int(line)
    ## TODO: We will return (output) the processed line as an integer from this function. (Just uncomment)
    return integer

# This function can stay relatively unchanged for problems where every line contains a little more of the input.
# it will return a list of whatever parse_line is formating the lines into.
def parse_instructions(file_name):
    cleaned_line = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_line.append(parse_line(line))
    return cleaned_line

## TODO: Implement part 1 solution
def part_1():
    ## TODO: We want to calculate the resulting frequency by moving it up and down by the values in the input.

    # Get a list of the integers representing the frequency changes from the input file.
    integers = parse_instructions(INPUT_FILE_NAME)

    # Initially start the frequency at 0.
    frequency = 0

    ## TODO: For each frequency in the list integers, change frequency.
    for frequencyChange in integers:
        frequency += frequencyChange

    ## TODO: Return the resultant frequency.
    # return ...

## TODO: Implement part 2 solution
def part_2():
    ## TODO: We want to calculate the first frequency which is repeated.

    # Get a list of the integers representing the frequency changes from the input file.
    integers = parse_instructions(INPUT_FILE_NAME)

    # Initially start the frequency at 0.
    frequency = 0

    # Initialize an "empty set" called visitedFrequencies to keep track of which frequencies have been observed.
    visitedFrequencies = set([])

    ## TODO: Add frequency to the set, since we already visited it.
    # visitedFrequencies.add(...)

    ## TODO: Once code is working delete return None statement. (It's there to prevent an infinite loop for now.)
    return None

    while True:
        ## TODO: For each frequency in the list integers, change frequency, and check if it has been
        ## already encountered. Once the list is progressed entired through, the while loop will take us
        ## back to the start.
        for frequencyChange in integers:
            frequency += frequencyChange
            ## TODO: Return frequency if it has already been visited. (Remove continue once return is implemented)
            if frequency in visitedFrequencies:
                continue
                #return ...
            else:
                ## TODO: Add frequency to visitedFrequencies. (Ditto with the continue)
                continue
                ## ...



print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))

import collections

file_name = "Inputs/day2Input.txt"

file = open(file_name)

input = file.read()

lines = input.split('\n')



### Part 1
# def find_repeats(line, num):
#     mapping = collections.defaultdict(int)
#     for letter in line:
#         mapping[letter] += 1
#     return num in mapping.values()
#
# double_count = 0
# triple_count = 0
#
# for line in lines:
#     if find_repeats(line, 2):
#         double_count += 1
#     if find_repeats(line, 3):
#         triple_count += 1
#
# check_sum = double_count * triple_count
#
# print(check_sum)


### Part 2

sorted_lines = sorted(lines)

prev_line = ['.' for _ in range(26)]

for line in sorted_lines:
    differences = 0
    similarities = ''
    for idx in range(len(line)):
        if line[idx] != prev_line[idx]:
            differences += 1
        else:
            similarities += line[idx]
        if differences > 1:
            break
    if differences == 1:
        print similarities
    prev_line = line


