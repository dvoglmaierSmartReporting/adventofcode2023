# part 1

with open("./day14/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day14/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

columns = [[] for _ in Lines[0]]

for line in Lines:
    for i, l in enumerate(line):
        if l == "O":
            columns[i].append(1)
        elif l == ".":
            columns[i].append(0)
        else:
            columns[i].append(-1)


# tilt north
for i, column in enumerate(columns):
    prepare, reordered = list(), list()
    no_rock = 1

    for j, col in enumerate(column):
        prepare.append(col)

        if (col < 0) or (j == len(columns) - 1):
            no_rock = 0

            prepare.sort(reverse=True)
            reordered += prepare

            prepare = list()

    if no_rock:
        prepare.sort(reverse=True)
        reordered = prepare.copy()

    columns[i] = reordered.copy()


length = len(columns[0])
result1 = sum([c * length - n for col in columns for n, c in enumerate(col) if c > 0])
print(f"{result1 = }")

# ---------------------------------------------------------
# part 2

# with open("./day14/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

columns = [[] for _ in Lines[0]]
for line in Lines:
    for i, l in enumerate(line):
        if l == "O":
            columns[i].append(1)
        elif l == ".":
            columns[i].append(0)
        else:
            columns[i].append(-1)


def tilt_north(columns: list[list]) -> list[list]:
    for i, column in enumerate(columns):
        prepare, reordered = list(), list()
        no_rock = 1

        for j, col in enumerate(column):
            prepare.append(col)

            if (col < 0) or (j == len(columns) - 1):
                no_rock = 0

                prepare.sort(reverse=True)
                reordered += prepare

                prepare = list()

        if no_rock:
            prepare.sort(reverse=True)
            reordered = prepare.copy()

        columns[i] = reordered.copy()

    return columns


def rotate_90_degree(columns: list[list]) -> list[list]:
    expected = [[] for _ in columns[0]]
    for column in columns[::-1]:
        for i, col in enumerate(column[::-1]):
            expected[i] = [col] + expected[i]

    return expected


def total_load(columns: list[list]) -> int:
    length = len(columns[0])
    return sum([c * length - n for col in columns for n, c in enumerate(col) if c > 0])


# start cycles
cycles = 300  # guess needed cycles to enter symmetry

loads = list()
for i in range(cycles):
    for _ in range(4):
        columns = tilt_north(columns)
        columns = rotate_90_degree(columns)

    loads.append(total_load(columns))


# find symmetries
scan = 15
found = 0
for loop_start, _ in enumerate(loads):
    for loop_length, _ in enumerate(loads[loop_start + 1 :]):
        if (
            loads[slice(loop_start, loop_start + scan)]
            == loads[
                slice(loop_start + 1 + loop_length, loop_start + 1 + loop_length + scan)
            ]
        ):
            found = 1
            break
    if found:
        break

# from symmetry project one billion cycles
cycle_modulo = (1_000_000_000 - (loop_start + 1)) % (loop_length + 1)
result2 = loads[loop_start + cycle_modulo]
print(f"{result2 = }")
