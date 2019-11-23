import collections

# TODO Read through the day 1 problem of 2018, then you can go through this file and try to implement the given
# suggestions to make the code work! (Delete all TODOs when finished.)


## TODO Change file path to appropriate input file.
INPUT_FILE_NAME = "Inputs/day2Input.txt"


# Having the string is already good enough, so this function is a no-op. (No operation)
def parse_line(line):
    return line

# This function can stay relatively unchanged for problems where every line contains a little more of the input.
# it will return a list of whatever parse_line is formating the lines into.
def parse_instructions(file_name):
    cleaned_line = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_line.append(parse_line(line))
    return cleaned_line

## TODO: Make a helper function! (Let's make a function that will tell us if an ID has the right number of repeated letters)
def has_x_repeats(x, id):
    # Lets make a dictionary to count the number of times a letter is repeated.
    # A default dictionary has the property that if the inputted thing has no
    repeats = collections.defaultdict(int)

    ## TODO: For each letter in id, count it in repeats
    for letter in id:
        repeats[letter] += 1
        continue

    # The method values returns a list of the values in the dictionary it is called on. For repeats this results in
    # a list of counts.
    counts = repeats.values()

    # If x is in counts, then that means there was a letter that appeared x times in id.
    has_x = x in counts

    ## TODO: Return the boolean value of whether id has a letter repeated x times.
    return has_x


## TODO: Implement part 1 solution
def part_1():
    ## TODO: We want to calculate the resulting frequency by moving it up and down by the values in the input.

    # Get a list of the integers representing the frequency changes from the input file.
    boxIds = parse_instructions(INPUT_FILE_NAME)

    ## TODO: Initialize two counters for the number of ids with 2 or 3 repeated letters.
    repeat_2 = 0
    repeat_3 = 0

    ## TODO: For each id in the list boxIds, increment the relevent counters.
    for boxId in boxIds:
        if has_x_repeats(2, boxId):
            repeat_2 += 1
        if has_x_repeats(3, boxId):
            repeat_3 += 1

    ## TODO: Calculate the checksum.
    checksum = repeat_2 * repeat_3


    ## TODO: Return the resultant frequency.
    return checksum

## TODO: Implement part 2 solution
def part_2():
    ## TODO: We want to find the two ids which differ by only 1 letter. It is inefficient to check every pair, so
    ## we will start by sorting

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