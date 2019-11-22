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


