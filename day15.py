from re import findall

with open("./day15/input.txt", "r") as fin:
    sequences = fin.readlines()
    sequences = [x.strip() for x in sequences]

with open("./day15/inputexample.txt", "r") as fin:
    sequences = fin.readlines()
    sequences = [x.strip() for x in sequences]

sequences = sequences[0].split(",")


def HASH(sequence: str) -> int:
    current = 0
    for seq in sequence:
        # algorithm
        current += ord(seq)  # character to ascii int
        current *= 17
        current = current % 256
    return current


steps = list()
for sequence in sequences:
    steps.append(HASH(sequence))

result1 = sum(steps)
print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

with open("./day15/input.txt", "r") as fin:
    sequences = fin.readlines()
    sequences = [x.strip() for x in sequences]

# with open("./day15/inputexample.txt", "r") as fin:
#     sequences = fin.readlines()
#     sequences = [x.strip() for x in sequences]

sequences = sequences[0].split(",")

boxes = [[] for _ in range(256)]

for sequence in sequences:
    label = findall(r"^\w+", sequence)
    label = label[0]

    box = boxes[HASH(label)]

    if "-" in sequence:
        to_remove = [label + " " + str(i) for i in range(1, 10)]
        for lens in list(set(box) & set(to_remove)):
            box.remove(lens)

    else:
        focal = findall(r"\d", sequence)
        focal = focal[0]

        content = [b.split(" ")[0] for b in box]
        if label in content:
            idx = content.index(label)
            box[idx] = label + " " + str(focal)
            continue

        box.append(label + " " + str(focal))

result2 = 0
for i, box in enumerate(boxes):
    if box == []:
        continue

    for j, b in enumerate(box):
        result2 += (i + 1) * (j + 1) * int(b[-1])

print(f"{result2 = }")
