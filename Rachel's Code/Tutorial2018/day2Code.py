import collections

# TODO Read through the day 2 problem of 2018, then you can go through this file and try to implement the given
# suggestions to make the code work! (Delete all TODOs when finished.)

## TODO: Edit the input file to match your input.
## TODO Change file path to appropriate input file.
INPUT_FILE_NAME = "Inputs/dayXInput.txt"


# Having the string is already good enough, so this function is a no-op. (No operation)
def parse_line(line):
    return line

#TODO: Make sure you understand this function
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
        # repeats[letter] += ...
        continue

    # The method values returns a list of the values in the dictionary it is called on. For repeats this results in
    # a list of counts.
    counts = repeats.values()

    # If x is in counts, then that means there was a letter that appeared x times in id.
    has_x = x in counts

    ## TODO: Return the boolean value of whether id has a letter repeated x times.
    # return ...


## TODO: Implement part 1 solution
def part_1():
    ## TODO: We want to calculate the resulting frequency by moving it up and down by the values in the input.

    # Get a list of the integers representing the frequency changes from the input file.
    boxIds = parse_instructions(INPUT_FILE_NAME)

    ## TODO: Initialize two counters for the number of ids with 2 or 3 repeated letters. (Start at 0)
    # repeat_2 = ...
    # repeat_3 = ...

    ## TODO: For each id in the list boxIds, increment the relevent counters.
    for boxId in boxIds:
        if has_x_repeats(2, boxId):
            # repeat_2 += ...
            pass ## TODO: Delete this line
        if has_x_repeats(3, boxId):
            # repeat_3 += ...
            pass ## TODO: Delete this line

    ## TODO: Calculate the checksum.
    # checksum = ...


    ## TODO: Return the resultant checksum.
    # return ...

## TODO: Implement a function which counts the number of differences between two ids.
def count_differences(id1, id2):
    differences = 0
    for letter1, letter2 in zip(id1, id2): # The zip function returns a list of pairs, so that letter1 and letter2 are from id1 and id2.
        if letter1 != letter2:
            # differences += ...
            pass
    return differences

## TODO: Implement a function which returns the common letters between the two ids.
def common_letters(id1, id2):
    common = ""
    # for letter1, letter2 in ...:
    #     if letter1 == letter2:
    #         common += letter1
    # return common

## TODO: Implement part 2 solution
def part_2():
    ## TODO: We want to find the two ids which differ by only 1 letter. It is inefficient to check every pair, so
    ## we will start by sorting the ids alphabetically, so that only consecutive ids could be a valid pair.

    # Get a list of the integers representing the frequency changes from the input file.
    boxIds = parse_instructions(INPUT_FILE_NAME)

    # Sort the box ids alphabetically.
    sortedBoxIds = sorted(boxIds)

    # Initialize an index to store the matching in.
    matchIdx = None

    ## TODO Go through the ids in the sorted list, until two consecutive ids differ in only one location.
    for idx in range(len(boxIds) - 1):
        # if count_differences(sortedBoxIds[idx], sortedBoxIds[idx + 1]) == ...:
        #     matchIdx = ...
        #     break
        pass ## TODO: Delete this file.

    ## TODO: Initialize inCommon to be the common letters between the two relevent ids in sortedBoxIds.
    # inCommon = ...
    inCommon = None ## TODO: Delete this line.

    return inCommon


print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))