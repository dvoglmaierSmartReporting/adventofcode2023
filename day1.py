from re import findall

with open("./day1/input1.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day1/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

digits = [findall(r"\d", line) for line in Lines]

result1 = sum([int(coord[0]) * 10 + int(coord[-1]) for coord in digits])

print(f"{result1 = }")

# ---------------------------------------------------------
# part 2

# with open("./day1/inputexample2.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

numbers = [
    findall(r"\d|one|two|three|four|five|six|seven|eight|nine", line) for line in Lines
]

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

d = dict([(word, i + 1) for i, word in enumerate(words)])

coordinates_parts = [[coord[0], coord[-1]] for coord in numbers]

coordinates_mapped = [
    [d[c] if len(c) > 1 and type(c) == str else int(c) for c in coords]
    for coords in coordinates_parts
]

result2 = sum([int(coord[0]) * 10 + int(coord[-1]) for coord in coordinates_mapped])

print(f"{result2 = }")
