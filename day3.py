# part 1

from re import findall, finditer

with open("./day3/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day3/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

result1 = 0

# read line with previous and following line; at the edges use '.' instead
for n, line in enumerate(Lines):
    if 0 < n < len(Lines) - 1:
        line_before = Lines[n - 1]
        line_after = Lines[n + 1]

    else:
        if n == 0:
            line_before = "." * len(line)
            line_after = Lines[n + 1]

        else:
            line_before = Lines[n - 1]
            line_after = "." * len(line)

    pos = 0

    for number in findall(r"\d+", line):
        # shift pos to search only the unsearched part of the line
        pos += line[pos:].find(number)

        search = slice(max(pos - 1, 0), min(pos + len(number) + 1, len(line)))
        area = line[search] + line_before[search] + line_after[search]

        pos += len(number)

        # find anything that's not a digit or '.'
        if findall(r"[^\d.]", area):
            result1 += int(number)

print(f"{result1 = }")

# ---------------------------------------------------------
# part 2

# with open("./day3/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

result2 = 0

# read line with previous and following line; at the edges use '.' instead
for n, line in enumerate(Lines):
    if 0 < n < len(Lines) - 1:
        line_before = Lines[n - 1]
        line_after = Lines[n + 1]

    else:
        if n == 0:
            line_before = "." * len(line)
            line_after = Lines[n + 1]

        else:
            line_before = Lines[n - 1]
            line_after = "." * len(line)

    pos = 0

    for gear in findall(r"\*", line):
        # shift pos to search only the unsearched part of the line
        pos += line[pos:].find(gear)

        # find overlap of gear span with all numbers in three lines
        gear_span = [pos - 1, pos, pos + 1]

        numbers = [
            number[0]
            for l in [line_before, line, line_after]
            for number in finditer(r"\d+", l)
            if number.start(0) in gear_span or number.end(0) - 1 in gear_span
        ]

        pos += 1

        # calculate gear ratio if two numbers found
        if len(numbers) == 2:
            result2 += int(numbers[0]) * int(numbers[1])

print(f"{result2 = }")
