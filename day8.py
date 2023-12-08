# part 1

from re import findall

with open("./day8/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day8/inputexample1.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

# with open("./day8/inputexample2.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

turns, lines = Lines[0], Lines[2:]

mapp = dict()
for line in lines:
    tmp = findall(r"\w+", line)
    mapp[tmp[0]] = {"L": tmp[1], "R": tmp[2]}

start, end = "AAA", "ZZZ"
result1 = 0

while 1:
    turn = turns[result1 % len(turns)]
    start = mapp[start][turn]

    result1 += 1

    if start == end:
        break

print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

# with open("./day8/inputexample3.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

turns, lines = Lines[0], Lines[2:]

mapp = dict()
for line in lines:
    tmp = findall(r"\w+", line)
    mapp[tmp[0]] = {"L": tmp[1], "R": tmp[2]}

starts = [key for key in mapp.keys() if "A" in key[2]]

frequences = list()

for start in starts:
    counter = 0
    hits = list()

    while 1:
        turn = turns[counter % len(turns)]
        start = mapp[start][turn]

        counter += 1

        if start[2] == "Z":
            hits.append(counter)

            # looking for sequence length
            if len(hits) >= 2:
                diff = hits[-1] - hits[-2]

                if hits[0] == diff:
                    frequences.append(hits[0])
                    break


# use prime factorization to find first possible step
# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


primes = [factor for freq in frequences for factor in prime_factors(freq)]
primes = list(set(primes))

result2 = 1
for prime in primes:
    result2 *= prime

print(f"{result2 = }")
