INPUT_FILE_NAME = "day1Input2017"

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
    cumsum = 0
    string = parse_instructions(INPUT_FILE_NAME)[0]
    print(string)
    print(range(len(string)-1))
    for i in range(len(string)-1):
        print(string[i])
        if int(string[i]) == int(string[i + 1]):
            cumsum += int(string[i])
    if int(string[0]) == int(string[len(string)-1]):
        cumsum += int(string[0])
    return cumsum

def part_2():
    cumsum = 0
    string = parse_instructions(INPUT_FILE_NAME)[0]
    half = int((len(string)) / 2)
    print(half)
    for i in range(len(string)-1):
        if i < half:
            if int(string[i]) == int(string[i + half]):
                cumsum += int(string[i])
        elif i >= half:
            if int(string[i]) == int(string[i - half]):
                cumsum += int(string[i])

        # if int(string[0]) == int(string[len(string)-1]):
        #     cumsum += int(string[0])
    return cumsum













print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))