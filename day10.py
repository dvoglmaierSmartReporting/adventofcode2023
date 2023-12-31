# part 1

from collections import deque
from itertools import product

with open("./day10/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day10/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

# with open("./day10/inputexample2.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]


matrix = [[l for l in line] for line in Lines]


def solve(matrix: list[list]) -> list:
    found = 0
    for i, mat in enumerate(matrix):
        for j, m in enumerate(mat):
            if "S" == m:
                found = 1
                break
        if found:
            break

    end_script = 0

    # mimic start letter for different directions
    snakes = [[(i, j)]] * 4
    mimic = {0: 3, 1: 6, 2: 9, 3: 12}
    # way: clock directions

    for k, path in enumerate(snakes):
        way = mimic[k]

        snake = deque(path)

        while snake:
            j, i = snake.popleft()

            parts = {3: (i + 1, j), 6: (i, j + 1), 9: (i - 1, j), 12: (i, j - 1)}
            y, x = parts[way]

            letter = matrix[x][y]

            if letter == "S":
                end_script = 1
                break

            if (
                (way == 3 and letter in ["-", "J", "7"])
                or (way == 6 and letter in ["|", "L", "J"])
                or (way == 9 and letter in ["-", "L", "F"])
                or (way == 12 and letter in ["|", "7", "F"])
            ):
                snake.append((x, y))
                path.append((x, y))

            # set new way for next iteration
            if (way == 6 and letter == "L") or (way == 12 and letter == "F"):
                way = 3
            elif (way == 3 and letter == "7") or (way == 9 and letter == "F"):
                way = 6
            elif (way == 6 and letter == "J") or (way == 12 and letter == "7"):
                way = 9
            elif (way == 3 and letter == "J") or (way == 9 and letter == "L"):
                way = 12

        if end_script:
            return path


path = solve(matrix)

result1 = len(path) // 2
print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

with open("./day10/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day10/inputexample3.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

# with open("./day10/inputexample4.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]


matrix = [[l for l in line] for line in Lines]

path = solve(matrix)


def find_way(point_one: tuple, point_two: tuple) -> int:
    y_one, x_one = point_one
    y_two, x_two = point_two
    y_dist, x_dist = y_two - y_one, x_two - x_one
    # return clock direction
    if x_dist == 1:
        return 3
    elif y_dist == -1:
        return 6
    elif x_dist == -1:
        return 9
    elif y_dist == 1:
        return 12


def collect_turns(path: list) -> dict:
    turns = {"left": 0, "right": 0}
    for i, p_three in enumerate(path[2:]):
        way_one = find_way(path[i], path[i + 1])
        way_two = find_way(path[i + 1], p_three)
        if way_one == way_two:
            continue
        elif ((way_one < way_two) and not (way_one == 3 and way_two == 12)) or (
            way_one == 12 and way_two == 3
        ):
            way = "left"
        elif ((way_one > way_two) and not (way_one == 12 and way_two == 3)) or (
            way_one == 3 and way_two == 12
        ):
            way = "right"
        turns[way] += 1
    return turns


turns = collect_turns(path)


def get_surrounding(point: tuple) -> list:
    y, x = point
    return [
        p
        for p in product([y + 1, y, y - 1], [x + 1, x, x - 1])
        if not (p[0] == y and p[1] == x)
    ]


# find rotation and force clockwise
if turns["left"] >= turns["right"]:
    print("counter-clockwise -> revert")
    path = path[::-1]
else:
    print("clockwise")


# coordinates which are not on path
inner = list(product(range(len(matrix)), range(len(matrix[0]))))
inner = list(set(inner) - set(path))

# exclude edges
exclude = list()
to_check = deque()
max_row, max_col = len(matrix) - 1, len(matrix[0]) - 1

for I_y, I_x in inner:
    if I_y == 0 or I_y == max_row or I_x == 0 or I_x == max_col:
        to_check.append((I_y, I_x))
        exclude.append((I_y, I_x))

while to_check:
    check = get_surrounding(to_check.popleft())

    intersect = list(set(inner) & set(check))
    overlap = list(set(exclude) & set(intersect))

    if 0 <= len(overlap) < len(intersect):
        exclude.extend(list(set(intersect) - set(overlap)))
        to_check.extend(list(set(intersect) - set(overlap)))


inner = list(set(inner) - set(exclude))


# detect groups of inner coordinates
groups, done = list(), list()
for I in inner:
    if I in done:
        continue

    overlap = list(set(get_surrounding(I)) & set(inner))
    done.append(I)

    if len(overlap) == 0:
        groups.append([I])
        continue

    group = list(overlap) + [I]

    expand = deque(group)
    while expand:
        e = expand.popleft()
        done.append(e)

        overlap = list(set(get_surrounding(e)) & set(inner))

        expand.extend(list(set(overlap) - set(group)))
        group.extend(list(set(overlap) - set(group)))

    groups.append(group)


result2 = 0

# check with direction the path circles a group
# if left-way, its outter: ignore
# if right-way, its inner: add to result2
for group in groups:
    circle = list()
    for g in group:
        check = list(set(get_surrounding(g)) - set(group))

        circle.extend(check)

    circle = list(set(circle))

    start, counter = 0, 0
    turns = {"left": 0, "right": 0}

    for i, p in enumerate(path[:-1]):
        if p in circle:
            start = 1
            if counter == 0:
                run = i

            counter += 1
            if counter == len(circle):
                break

        if start:
            way_one = find_way(path[i - 1], p)
            way_two = find_way(p, path[i + 1])

            if way_one == way_two:
                continue
            elif ((way_one < way_two) and not (way_one == 3 and way_two == 12)) or (
                way_one == 12 and way_two == 3
            ):
                way = "left"
            elif ((way_one > way_two) and not (way_one == 12 and way_two == 3)) or (
                way_one == 3 and way_two == 12
            ):
                way = "right"

            turns[way] += 1

    # most group turns differ by 2 or 3
    # if difference is larger, there might be an issue in the logic (not sure yet)
    if (turns["right"] > turns["left"]) and (turns["right"] - turns["left"] <= 3):
        result2 += len(group)


print(f"{result2 = }")
