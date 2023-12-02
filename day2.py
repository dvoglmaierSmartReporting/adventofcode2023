from re import findall

with open("./day2/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day2/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

possible = 0
max_red_allowed = 12
max_green_allowed = 13
max_blue_allowed = 14

for line in Lines:
    parts = line.split(": ")

    game_id = int(findall(r"\d+", parts[0])[0])

    max_red_found = max([int(i) for i in findall(r"\d+(?=\sred)", parts[1])])

    max_green_found = max([int(i) for i in findall(r"\d+(?=\sgreen)", parts[1])])

    max_blue_found = max([int(i) for i in findall(r"\d+(?=\sblue)", parts[1])])

    if (
        not max_red_found > max_red_allowed
        and not max_green_found > max_green_allowed
        and not max_blue_found > max_blue_allowed
    ):
        possible += game_id

result1 = possible

print(f"{result1 = }")

# ---------------------------------------------------------
# part 2

# with open("./day2/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

summe = 0

for line in Lines:
    parts = line.split(": ")

    max_red_found = max([int(i) for i in findall(r"\d+(?=\sred)", parts[1])])

    max_green_found = max([int(i) for i in findall(r"\d+(?=\sgreen)", parts[1])])

    max_blue_found = max([int(i) for i in findall(r"\d+(?=\sblue)", parts[1])])

    summe += max_red_found * max_green_found * max_blue_found

result2 = summe

print(f"{result2 = }")
