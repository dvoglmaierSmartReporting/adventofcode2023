# part 1

with open("./day11/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day11/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]


# add horizontal space
Lines_hor_added = list()
for line in Lines:
    Lines_hor_added.append(line)
    if not ("#" in line):
        Lines_hor_added.append(line)

# add vertical space
Lines_vert_added = [[] for _ in Lines_hor_added]
for i, _ in enumerate(Lines_hor_added[0]):
    column = [line[i] for line in Lines_hor_added]
    for j, line in enumerate(Lines_hor_added):
        Lines_vert_added[j] += line[i]
    if not ("#" in column):
        for j, line in enumerate(Lines_hor_added):
            Lines_vert_added[j] += line[i]
Lines = Lines_vert_added.copy()

# rename galaxies by incrementing number
# collect galaxies in dict
increment = 1
galaxies = dict()
for i, line in enumerate(Lines):
    for j, l in enumerate(line):
        if l == "#":
            Lines[i][j] = str(increment)
            galaxies[increment] = (i, j)

            increment += 1

pairs = [
    (a, b) for i, a in enumerate(range(1, increment)) for b in range(i + 1, increment)
]


# create function to calculate Manhattan distance
def manhattan(a, b):
    return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


result1 = 0
for start, target in pairs:
    result1 += manhattan(galaxies[start], galaxies[target])

print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

with open("./day11/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day11/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]


# rename galaxies by incrementing number
# collect galaxies in dict
increment = 1
galaxies = dict()
for i, line in enumerate(Lines):
    for j, l in enumerate(line):
        if l == "#":
            galaxies[increment] = (i, j)

            increment += 1


ys = set([g_y for g_y, _ in galaxies.values()])
xs = set([g_x for _, g_x in galaxies.values()])

empty_ys = sorted(set(range(len(Lines))) - ys)
empty_xs = sorted(set(range(len(Lines[0]))) - xs)

space = 9  # 1030
space = 99  # 8410
space = 1_000_000 - 1

# vertically shift galaxy coordinates
runs = 0
for y in empty_ys:
    for key, galaxy in galaxies.items():
        if galaxy[0] > y + space * runs:
            galaxies[key] = (galaxy[0] + space, galaxy[1])
    runs += 1

# horizontally shift galaxy coordinates
runs = 0
for x in empty_xs:
    for key, galaxy in galaxies.items():
        if galaxy[1] > x + space * runs:
            galaxies[key] = (galaxy[0], galaxy[1] + space)
    runs += 1

pairs = [
    (a, b) for i, a in enumerate(range(1, increment)) for b in range(i + 1, increment)
]

result2 = 0
for start, target in pairs:
    result2 += manhattan(galaxies[start], galaxies[target])

print(f"{result2 = }")
