from collections import Counter


def load_crates(part: int):
    with open(f"input_{part}.txt") as f:
        return list(map(int, f.read().strip().split(",")))


print("Part 1:", sum(set(load_crates(1))))
print("Part 2:", sum(sorted(set(load_crates(2)))[:20]))
print("Part 3:", max(Counter(load_crates(3)).values()))
