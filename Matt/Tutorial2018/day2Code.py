import collections as c



## TODO Change file path to appropriate input file.
INPUT_FILE_NAME = "Inputs/day2Input.txt"

## TODO Implement per line interpretation of input (If applicable)
def parse_line(line):
    return line

def parse_instructions(file_name):
    cleaned_line = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_line.append(parse_line(line))
    return cleaned_line

## TODO Implement part 1 solution
def part_1():
    idlist = parse_instructions(INPUT_FILE_NAME)


    numtwos = 0
    numthrees = 0

    for id in idlist:
        dick = c.defaultdict(int)
        for idletter in id:
            dick[idletter] += 1
        iddickvallist = dick.values()
        if 2 in iddickvallist:
            numtwos += 1
        if 3 in iddickvallist:
            numthrees += 1
        # for iddickval in iddickvallist:
        #     if iddickval == 2:
        #         numtwos += 1
        #     elif iddickval == 3:
        #         numthrees += 1
    return numthrees * numtwos

## TODO Implement part 2 solution
def part_2():
    pass


print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))


