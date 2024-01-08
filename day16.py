# part 1

from collections import deque

with open("./day16/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day16/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]


matrix = [[l for l in line] for line in Lines]


def solve(start: tuple, matrix: list[list]) -> int:
    beams = deque([[start]])

    n, trajectories = 0, []

    while beams:
        beam = beams.popleft()

        trajectories.append(beam)

        y, x, clock = beam[0]

        store_set = 0
        while True:
            if clock == 3:
                x += 1
            elif clock == 6:
                y += 1
            elif clock == 9:
                x -= 1
            else:
                y -= 1

            if not (0 <= y < len(matrix) and 0 <= x < len(matrix[0])):
                break

            field = matrix[y][x]

            if field == ".":
                trajectories[n].append((y, x, clock))
            elif field == "|":
                if clock in [6, 12]:
                    trajectories[n].append((y, x, clock))

                else:
                    clock = 12
                    trajectories[n].append((y, x, clock))

                    # create new beam path if start doesn't exist yet
                    starts = [t[0] for t in trajectories]
                    if not (y, x, 6) in starts:
                        beams.append([(y, x, 6)])

            elif field == "-":
                if clock in [3, 9]:
                    trajectories[n].append((y, x, clock))

                else:
                    clock = 9
                    trajectories[n].append((y, x, clock))

                    # create new beam path if start doesn't exist yet
                    starts = [t[0] for t in trajectories]
                    if not (y, x, 3) in starts:
                        beams.append([(y, x, 3)])

            elif field == "/":
                if clock == 3:
                    clock = 12
                elif clock == 6:
                    clock = 9
                elif clock == 9:
                    clock = 6
                else:
                    clock = 3
                trajectories[n].append((y, x, clock))

            elif field == "\\":
                if clock == 3:
                    clock = 6
                elif clock == 6:
                    clock = 3
                elif clock == 9:
                    clock = 12
                else:
                    clock = 9
                trajectories[n].append((y, x, clock))

            # prevent loops
            if store_set == set(trajectories[n]):
                break
            store_set = set(trajectories[n])

        n += 1

    zeros = [[0 for _ in line] for line in Lines]

    # remove start element
    trajectories[0] = trajectories[0][1:]

    for trajectory in trajectories:
        for y, x, _ in trajectory:
            zeros[y][x] = 1

    return sum([sum(row) for row in zeros])


start = (0, -1, 3)  # ( row, columns, clock direction)

result1 = solve(start, matrix)
print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

with open("./day16/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day16/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

matrix = [[l for l in line] for line in Lines]

result2 = 0

# left edge
for y in range(len(matrix)):
    start = (y, -1, 3)

    energy = solve(start, matrix)
    result2 = max(result2, energy)

# right edge
for y in range(len(matrix)):
    start = (y, len(matrix), 9)

    energy = solve(start, matrix)
    result2 = max(result2, energy)

# top edge
for x in range(len(matrix[0])):
    start = (-1, x, 6)

    energy = solve(start, matrix)
    result2 = max(result2, energy)

# bottom edge
for x in range(len(matrix[0])):
    start = (len(matrix[0]), x, 12)

    energy = solve(start, matrix)
    result2 = max(result2, energy)

print(f"{result2 = }")
