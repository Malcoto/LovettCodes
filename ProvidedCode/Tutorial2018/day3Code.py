# TODO Read through the day 3 problem of 2018, then you can go through this file and try to implement the given
# suggestions to make the code work! (Delete all TODOs when finished.)

import collections

## TODO Change file path to appropriate input file. (Replace the X)
INPUT_FILE_NAME = "Inputs/dayXInput.txt"

# Initialize an empty default dictionary, which will return an integer if you try to look up a key
# that is not yet in the dictionary
global grid = collections.defaultdict(int)

## TODO" First we will write a function that can process the character inputs line
# by line. We will cast these strings to an integer by calling int(line).
def parse_line(line):
    # The variable line is of type string. The information we care about, though, is
    # numeric by nature, meaning we should cast to an integer.
    
    ## TODO: Figure out how you need to preprocess the line to get the important
    ## information we use below.

    ## TODO: Uncomment, then complete the lines below.
    # left = int(...) 
    # top = int(...)
    # width = int(...)
    # height = int(...)
    
    return left, top, width, height

# This function can stay relatively unchanged for problems where every line contains a little more of the input.
# it will return a list of whatever parse_line is formating the lines into.
def parse_instructions(file_name):
    cleaned_line = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_line.append(parse_line(line))
    return cleaned_line

### Part 1
def part_1():
    
    # Get a list of the integers representing the elf fabric grid from the input file.
    lines = parse_instructions(INPUT_FILE_NAME)    

    for line in lines:

        ## TODO: find the relevant information from the parsed line return values
        
        ## TODO: go through each row using the width and the height from the parsed line
        for row in range(width):
           
            for col in range(height):
                
                ## TODO: Increment the grid cell to represent a claim by uncommenting and completing 
                ## the following line
                # grid[(...,...)] += ...

### Part 2
def part_2():
    
    # Get a list of the integers representing the elf fabric grid from the input file.
    lines = parse_instructions(INPUT_FILE_NAME)    
   
    for line in lines:

        ## TODO: find the relevant information from the parsed line return values and some way to track
        ## overlapping claims -- the most effective way is likely with a boolean (true/false)!

        for row in range(width):

            for col in range(height):

                ## TODO: rewrite and uncomment the line below to check if the current cell is doubly
                ## claimed, and update your tracking to reflect that

                # if gridcell is doubly claimed:

                    ## TODO: update the doubly claimed tracker
                    # break
        
        ## TODO: If no cells are doubly claimed then print out the line
        # if not doubly claimed:
            print("Part 2 line answer: {}".format(line))

# Running the code!
part_1()
part_2()