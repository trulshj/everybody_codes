from utils.input import readlines_input
from dataclasses import dataclass


@dataclass(frozen=True)
class Catapult:
    name: str
    row: int
    col: int
    score: int


def calculate_shot(catapult: Catapult, strength: int):
    hits = set()
    y, x = catapult.row, catapult.col
    for _ in range(strength):
        y += 1
        x += 1
        hits.add((y, x))
    for _ in range(strength):
        x += 1
        hits.add((y, x))
    while y > 0:
        y -= 1
        x += 1
        hits.add((y, x))
    return hits


def parse_input(part: int):
    lines = [x.rstrip() for x in readlines_input(12, part)][::-1]
    targets = set()
    target_healths = {}
    catapult = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char in "T":
                targets.add((row, col))
                target_healths[(row, col)] = 1
            if char in "H":
                targets.add((row, col))
                target_healths[(row, col)] = 2
            elif char in "ABC":
                catapult.add(Catapult(name=char, row=row,
                             col=col, score=ord(char)-64))

    return catapult, targets, target_healths


def find_target(catapult: Catapult, targets: set[tuple[int, int]], target_healths: dict[tuple[int, int], int]):
    if len(targets) == 0:
        return None, 0

    MAX_STRENGTH = max(targets, key=lambda x: x[1])[1]
    strength = MAX_STRENGTH

    target_height = max(targets, key=lambda x: x[0])[0]
    potential_targets = set(filter(lambda x: x[0] == target_height, targets))
    while 0 < strength:
        potential_hits = calculate_shot(catapult, strength)
        for target in potential_targets:
            if target in potential_hits:
                target_healths[target] -= 1
                if target_healths[target] == 0:
                    targets.remove(target)
                return target, strength * catapult.score
        strength -= 1
    return None, 0


def solve(part: int):
    catapults, targets, target_healths = parse_input(part)
    catapults = sorted(list(catapults), key=lambda c: c.score)
    score = 0
    while targets:
        for catapult in catapults:
            _, s = find_target(catapult, targets, target_healths)
            score += s

    print(f"Part {part}: {score}")


def main():
    solve(1)
    solve(2)


if __name__ == "__main__":
    main()
