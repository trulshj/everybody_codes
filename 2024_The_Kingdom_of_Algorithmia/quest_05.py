from collections import deque, defaultdict
from math import ceil
from utils.input import readlines_input


def parse_input(part: int) -> list[deque[int]]:
    return list(map(deque, zip(*(map(int, line.split()) for line in readlines_input(5, part)))))


def do_dance(grid: list[deque[int]], column_idx: int):
    dancer = grid[column_idx].popleft()
    target_column = grid[(column_idx + 1) % len(grid)]
    rows = len(target_column)

    if ceil((dancer / rows)) % 2:
        target_idx = (dancer % rows) - 1
        target_column.insert(target_idx, dancer)
    else:
        target_idx = ((-dancer) % rows) + 1
        target_column.insert(target_idx, dancer)

    return int("".join(map(lambda x: str(x[0]), grid)))


def get_arrangement_key(x):
    return "".join(("".join(map(str, z))) for z in x)


def run_dance(part):
    arrangement = parse_input(part)
    round_idx = 0
    shouts = defaultdict(int)
    seen = set()

    while True:
        n = do_dance(arrangement, round_idx % len(arrangement))
        round_idx += 1
        shouts[n] += 1

        if (part == 1 and round_idx == 10):
            print(n)
            break

        if (part == 2 and shouts[n]) == 2024:
            print(n * round_idx)
            break

        if (part == 3):
            arrangement_key = get_arrangement_key(arrangement)
            if arrangement_key in seen:
                print(max(shouts.keys()))
                break
            else:
                seen.add(arrangement_key)


if __name__ == "__main__":
    run_dance(1)
    run_dance(2)
    run_dance(3)
