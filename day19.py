from collections import defaultdict, deque
from math import prod

with open("./day19/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day19/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]

rules_only, parts_only = list(), list()
to_rules = True

for line in Lines:
    if line == "":
        to_rules = False
        continue

    if to_rules:
        rules_only.append(line)
    else:
        parts_only.append(line)

parts = list()
for i, part in enumerate(parts_only):
    parts.append(defaultdict(lambda: {"x": 0, "m": 0, "a": 0, "s": 0}))

    part = part[1:-1]
    for p in part.split(","):
        att, val = p.split("=")

        parts[i][att] = int(val)


def extract_condition(rule: str) -> (str, str, int, str):
    # e.g. 'a<2006:qkq'

    if not ":" in rule:
        return "", "", "0", rule

    cat, op = rule[0], rule[1]
    rule = rule[2:]

    value, nxt = rule.split(":")
    return cat, op, value, nxt


rules = dict()
for rule in rules_only:
    key, rule = rule.split("{")
    rules[key] = rule[:-1]

for key, rule in rules.items():
    wf = rule.split(",")
    rules[key] = [extract_condition(w) for w in wf]


start = "in"
result1 = 0

for part in parts:
    queue = deque(rules[start])

    while queue:
        rule = queue.popleft()
        cat, op, value, nxt = rule

        if cat == "" or eval(str(part[cat]) + op + value):
            if nxt in ["A", "R"]:
                break

            for r in rules[nxt][::-1]:
                queue.appendleft(r)

    if nxt == "R":
        continue

    if nxt == "A":
        result1 += sum(part.values())

print(f"{result1 = }")


# ---------------------------------------------------------
# part 2

with open("./day19/input.txt", "r") as fin:
    Lines = fin.readlines()
    Lines = [x.strip() for x in Lines]

# with open("./day19/inputexample.txt", "r") as fin:
#     Lines = fin.readlines()
#     Lines = [x.strip() for x in Lines]


rules_only = list()

for line in Lines:
    if line == "":
        break

    rules_only.append(line)

rules = dict()
for rule in rules_only:
    key, rule = rule.split("{")

    wf = rule[:-1].split(",")

    rules[key] = [extract_condition(w) for w in wf]


def reduce_rule_complexity(rules: dict):
    # e.g. sj{x<1591:A,A} can be skipped

    for key, wf in rules.items():
        if set(rule[-1] for rule in wf) == {"A"}:
            del rules[key]

            for name, wf in rules.items():
                for i, rule in enumerate(wf):
                    cat, op, value, nxt = rule
                    if nxt == key:
                        rules[name][i] = (cat, op, value, "A")

                        return True
    return False


run = True
while run:
    run = reduce_rule_complexity(rules)


# recusive function until rule 'in'
def find_origin(rules: dict, path: list, target: str):
    for key, wf in rules.items():
        for i, rule in enumerate(wf):
            cat, op, value, nxt = rule

            if nxt == target:
                outcome = cat != ""
                path.append((rule, outcome))

                if i > 0:
                    for r in wf[i - 1 :: -1]:
                        path.append((r, False))

                if key == "in":
                    return path

                return find_origin(rules, path, key)


paths, seen = list(), set()
target = "A"

for key, wf in rules.items():
    for i, rule in enumerate(wf):
        cat, op, value, nxt = rule

        current = key + str(i)
        path = list()

        if nxt == target and not current in seen:
            outcome = cat != ""
            path.append((rule, outcome))

            if i > 0:
                for r in wf[i - 1 :: -1]:
                    path.append((r, False))

            # recusive function
            path = find_origin(rules, path, key)

            paths.append(path)

            seen = set(list(seen) + list(current))


conditions = list()

for path in paths:
    condition = list()

    for p in path:
        rule, outcome = p
        cat, op, value, _ = rule

        if cat == "":
            continue

        if not outcome and op == "<":
            op = ">="

        if not outcome and op == ">":
            op = "<="

        condition.append((cat, op, value))

    conditions.append(condition)


result2 = 0

for condition in conditions:
    options = defaultdict(lambda: slice(1, 4000))

    for l in ["x", "m", "a", "s"]:
        options[l]

    for c in condition:
        cat, op, val = c
        val = int(val)

        o = options[cat]

        if op == ">" and o.start < val < o.stop:
            options[cat] = slice(val + 1, o.stop)

        elif op == ">=" and o.start < val < o.stop:
            options[cat] = slice(val, o.stop)

        elif op == "<" and o.start < val < o.stop:
            options[cat] = slice(o.start, val - 1)

        elif op == "<=" and o.start < val < o.stop:
            options[cat] = slice(o.start, val)

        if val > o.stop:
            options[cat] = slice(o.start, o.stop)

    spans = [v.stop - v.start + 1 for v in options.values()]

    result2 += prod(spans)


print(f"{result2 = :_}")
