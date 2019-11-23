import collections

file_name = "Inputs/day3Input.txt"

file = open(file_name)

input = file.read()

lines = input.split('\n')

def parse_line(line):
    parts = line.split(' ')
    top_left = parts[2]
    ranges = parts[3]
    left = int(top_left.split(',')[0])
    top = int(top_left.split(',')[1].split(':')[0])
    width = int(ranges.split('x')[0])
    height = int(ranges.split('x')[1])
    return left, top, width, height

grid = collections.defaultdict(int)

### Part 1

for line in lines:
    coords =  parse_line(line)
    row_offset = coords[0]
    col_offset = coords[1]
    for row in range(coords[2]):
        for col in range(coords[3]):
            grid[(row + row_offset, col + col_offset)] += 1

### Part 2

for line in lines:
    coords =  parse_line(line)
    row_offset = coords[0]
    col_offset = coords[1]
    no_good = False
    for row in range(coords[2]):
        for col in range(coords[3]):
            if grid[(row + row_offset, col + col_offset)] > 1:
                no_good = True
                break
    if not no_good:
        print(line)