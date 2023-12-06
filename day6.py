# part 1

from re import findall
from math import sqrt, ceil, floor

with open("./day6/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day6/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

times = Lines[0].split("Time:")[1].strip()
times = findall(r"\d+", times)

distances = Lines[1].split("Distance:")[1].strip()
distances = findall(r"\d+", distances)

result1 = 1

for time, dist in zip(times, distances):
    time = int(time)
    dist = int(dist) + 1

    a, b, c = -1, time, -dist

    start = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
    start = ceil(start)

    end = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
    end = floor(end)

    result1 *= end - start + 1

print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

# with open("./day6/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

times = Lines[0].split("Time:")[1].strip()
time = int(''.join(findall(r"\d+", times)))

distances = Lines[1].split("Distance:")[1].strip()
distance = int(''.join(findall(r"\d+", distances))) + 1

a, b, c = -1, time, -distance

start = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
start = ceil(start)

end = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
end = floor(end)

result2 = end - start + 1

print(f"{result2 = }")
