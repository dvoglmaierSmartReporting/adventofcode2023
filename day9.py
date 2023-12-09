# part 1

from re import findall

with open("./day9/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day9/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

lines = [[int(d) for d in findall(r"-?\d+", line)] for line in Lines]

history = []

for line in lines:
    diff = [line.copy()]

    while 1:
        diff.append([y - x for x, y in zip(diff[-1][0::], diff[-1][1::])])

        if len(set(diff[-1])) == 1:
            break

    history.append(sum([d[-1] for d in diff]))

result1 = sum(history)
print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

# with open("./day9/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

lines = [[int(d) for d in findall(r"-?\d+", line)] for line in Lines]

history = []

for line in lines:
    diff = [line.copy()]

    while 1:
        diff.append([y - x for x, y in zip(diff[-1][0::], diff[-1][1::])])

        if len(set(diff[-1])) == 1:
            break

    new = 0
    for d in diff[::-1]:
        new = d[0] - new

    history.append(new)

result2 = sum(history)
print(f"{result2 = }")
