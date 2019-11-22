# TODO Go through the file and try to implement the given suggestions to make the code work!
# (Delete all TODOs when finished.)


## TODO Change file path to appropriate input file. (Replace the X)
INPUT_FILE_NAME = "Inputs/day1Input.txt"


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
    return frequency

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

    ## TODO: Once code

    while True:
        ## TODO: For each frequency in the list integers, change frequency, and check if it has been
        ## already encountered.
        for frequencyChange in integers:
            frequency += frequencyChange
            ## TODO: Return frequency if it has already been visited.
            if frequency in visitedFrequencies:
                return frequency
            else:
                ## TODO: Add frequency to visitedFrequencies.
                visitedFrequencies.add(frequency)



print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))