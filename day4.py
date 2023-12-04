# part 1

from re import findall

with open("./day4/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day4/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

result1 = 0

for line in Lines:
    winners, numbers = line.split(": ")[1].split("|")

    winners = findall(r"\d+", winners)
    numbers = findall(r"\d+", numbers)

    intersect = list(set(winners) & set(numbers))

    if len(intersect) > 0:
        result1 += pow(2, len(intersect) - 1)

print(f"{result1 = }")

# ---------------------------------------------------------
# part 2

# with open("./day4/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

result2 = 0

stack = [1] * len(Lines)

for i, line in enumerate(Lines):
    winners, numbers = line.split(": ")[1].split("|")

    winners = findall(r"\d+", winners)
    numbers = findall(r"\d+", numbers)

    intersect = list(set(winners) & set(numbers))

    if len(intersect) > 0:
        span = slice(i + 1, i + len(intersect) + 1)

        factor = stack[i]

        stack[span] = [v + 1 * factor for v in stack[span]]

result2 = sum(stack)

print(f"{result2 = }")
