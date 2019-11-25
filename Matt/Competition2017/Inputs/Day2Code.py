INPUT_FILE_NAME = "Day2Input.txt"

## TODO Implement per line interpretation of input (If applicable)
def parse_line(line):
    line = line.strip("\n").split("\t")
    return line

def parse_instructions(file_name):
    cleaned_matrix = []
    with open(file_name) as input_file:
        for line in input_file.readlines():
            cleaned_matrix.append(parse_line(line))
    return cleaned_matrix

def part_1():
    matrix = parse_instructions(INPUT_FILE_NAME)
    cumsum = 0
    for row in matrix:
        row = [int(strnum) for strnum in row]
        srow = sorted(row)
        rowsum = srow[len(srow)-1] - srow[0]
        cumsum += rowsum
    return cumsum

def part_2():
    matrix = parse_instructions(INPUT_FILE_NAME)
    cumsum = 0
    for row in matrix:
        row = [int(strnum) for strnum in row]
        row = sorted(row)
        row.reverse()
        print(row)
        #evens = [num for num in row if num % 2 == 0]
        length = range(len(row))
        for i in length:
            for j in range((i+1), (len(row))):
                if row[i] % row[j] == 0:
                    print(row[i])
                    print(row[j])
                    rowsum = row[i] / row[j]
                    print(rowsum)
                    cumsum += rowsum
    return cumsum






print("Part 1 answer: {}".format(part_1()))
print("Part 2 answer: {}".format(part_2()))