# part 1

from re import findall
from collections import deque
import time


# measure time
tic = time.time()


with open("./day5/input.txt", "r") as fin:
    Lines = fin.read().split("\n\n")

# with open("./day5/inputexample1.txt", "r") as fin:
#     Lines = fin.read().split("\n\n")

seeds = Lines.copy().pop(0).split(": ")[1]
seeds = [int(s) for s in findall(r"\d+", seeds)]

mapping = [
    [[int(n) for n in findall(r"\d+", k)] for k in m.split("\n")[1:]] for m in Lines
]

locations = []

for seed in seeds:
    location = int(seed)

    for mapp in mapping:
        for m in mapp:
            if location < m[1] or location > m[1] + m[2]:
                continue

            elif m[1] <= location <= m[1] + m[2]:
                location = m[0] + location - m[1]
                break

    locations.append(location)

result1 = min(locations)
print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

with open("./day5/input.txt", "r") as fin:
    Lines = fin.read().split("\n\n")

# with open("./day5/inputexample1.txt", "r") as fin:
#     Lines = fin.read().split("\n\n")

seeds_tmp = Lines.copy().pop(0).split(": ")[1]
seeds_tmp = [int(s) for s in findall(r"\d+", seeds_tmp)]

# create queue for seeds slices
seeds = deque()
while len(seeds_tmp):
    start, span = seeds_tmp.pop(0), seeds_tmp.pop(0)
    seeds.append(slice(start, start + span))  # slice( start, stop[ )


mapping = [
    [[int(n) for n in findall(r"\d+", k)] for k in m.split("\n")[1:]] for m in Lines
]
mapping = mapping[1:]

# mapp = [slice( start, stop[ ), target_slice( start, stop[ )]
mapping = [
    [[slice(m[1], m[1] + m[2]), slice(m[0], m[0] + m[2])] for m in mapp]
    for mapp in mapping
]


for mapp in mapping:
    # init queue for upcoming mapping
    next_seeds = deque()

    while seeds:
        seed = seeds.popleft()

        # if seed passes all map intervals without interaction,
        # don't forget to add it to new queue for next mapping
        walk_through = 1

        for m, target in mapp:
            # case: no overlap
            if (m.start >= seed.stop) or (seed.start >= m.stop):
                continue

            # case: partial overlap, interval before seed
            if (m.start <= seed.start) and (m.stop < seed.stop):
                walk_through = 0

                intersect = m.stop

                # add unshifted seed slice back into current queue
                unshifted = slice(intersect, seed.stop)
                seeds.append(unshifted)

                # add shifted seed slice for next queue
                shift = target.start - m.start
                shifted = slice(seed.start + shift, intersect + shift)
                next_seeds.append(shifted)

            # case: partial overlap, seed before interval
            if (seed.start < m.start) and (seed.stop <= m.stop):
                walk_through = 0

                intersect = m.start

                # add unshifted seed slice back into current queue
                unshifted = slice(seed.start, intersect)
                seeds.append(unshifted)

                # add shifted seed slice for next queue
                shift = target.start - m.start
                shifted = slice(intersect + shift, seed.stop + shift)
                next_seeds.append(shifted)

            # case: full overlap, shift seed slice
            if (m.start <= seed.start) and (m.stop >= seed.stop):
                walk_through = 0

                shift = target.start - m.start
                shifted = slice(seed.start + shift, seed.stop + shift)
                next_seeds.append(shifted)

        if walk_through:
            next_seeds.append(seed)

    seeds = next_seeds.copy()


result2 = min([seed.start for seed in next_seeds])
print(f"{result2 = }")


# toc
toc = time.time() - tic
print(f"{round(toc, 4)} seconds")
