import math


def gears(part: int):
    with open(f"input_{part}.txt") as f:
        gears = f.readlines()
        return int(gears[0]) / int(gears[-1])


def stacked_ratio(gear):
    lower, upper = gear.split("|")
    return int(upper) / int(lower)


def stacked_gears(part: int):
    with open(f"input_{part}.txt") as f:
        gears = f.readlines()
        return int(gears[0]) / int(gears[-1]) * math.prod(map(stacked_ratio, gears[1:-1]))


print("Part 1:", math.floor(gears(1)) * 2025)
print("Part 2:", math.ceil(1e13 / gears(2)))
print("Part 3:", math.floor(stacked_gears(3) * 100))
