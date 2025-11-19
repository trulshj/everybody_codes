from collections import defaultdict
from math import ceil


def read(part: int):
    with open(f"input_{part}.txt") as f:
        return f.read().rstrip()


def combinations(note: str):
    mentors = defaultdict(int)
    total = defaultdict(int)
    for c in note:
        if c in "ABC":
            mentors[c] += 1
        else:
            total[c] += mentors[c.upper()]
    return total


print("Part 1:", combinations(read(1))['a'])
print("Part 2:", sum(combinations(read(2)).values()))


note = read(3)
knights = defaultdict(list)

total = 0

for i, c in enumerate(note):
    if c in "abc":
        mentor = c.upper()
        for j in range(-1000, 1001):
            offset = i+j
            wrapped = offset % len(note)

            if note[wrapped] == mentor:
                adjust = len(note) - 1 - offset if offset < 0 else offset
                total += 1000 - adjust // len(note)

print("Part 3:", total)
