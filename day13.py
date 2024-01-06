with open("./day13/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day13/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]


def rows2columns(rows: list) -> list:
    columns = ["" for _ in rows[0]]

    for row in rows:
        for i, r in enumerate(row):
            columns[i] += r
    return columns


def prepare_areas(Lines: list) -> list[dict]:
    areas, rows, start = list(), list(), 0

    for i, line in enumerate(Lines):
        if not line == "":
            rows.append(line)

        if line == "" or i == len(Lines) - 1:
            areas.append({"rows": rows, "columns": rows2columns(rows)})
            rows = list()

    return areas


def solve_area(
    rows: list,
    columns: list,
    origin_i: int = -1,
    origin_j: int = -1,
) -> tuple:
    # these vars are added for part 2
    origin_i -= 1
    origin_j -= 1

    for i, row in enumerate(rows[:-1]):
        if row == rows[i + 1]:
            span = min(i + 1, len(rows) - (i + 1))

            before = rows[i + 1 - span : i + 1]
            before = before[::-1]
            after = rows[i + 1 : i + 1 + span]

            if before == after and i != origin_i:
                # horizontal mirror between {i+1} and {i+2}
                return i + 1, 0

    for j, column in enumerate(columns[:-1]):
        if column == columns[j + 1]:
            span = min(j + 1, len(columns) - (j + 1))

            left = columns[j + 1 - span : j + 1]
            left = left[::-1]
            right = columns[j + 1 : j + 1 + span]

            if left == right and j != origin_j:
                # vertical mirror between {j+1} and {j+2}
                return 0, j + 1
    return 0, 0


areas = prepare_areas(Lines)

result1 = 0
for area in areas:
    i, j = solve_area(*area.values())
    result1 += i * 100 + j

print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

with open("./day13/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day13/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

areas = prepare_areas(Lines)

result2 = 0
for area in areas:
    rows, columns = area.values()

    origin_i, origin_j = solve_area(rows, columns)
    for n, row in enumerate(rows):
        found = False

        for k, c in enumerate(row):
            if c == "#":
                char = "."
            else:
                char = "#"

            tmp_row = [row[:k] + char + row[k + 1 :]]
            tmp_rows = rows[:n] + tmp_row + rows[n + 1 :]

            i, j = solve_area(tmp_rows, rows2columns(tmp_rows), origin_i, origin_j)

            if i + j > 0:
                result2 += i * 100 + j
                found = True
                break
        if found:
            break

print(f"{result2 = }")
