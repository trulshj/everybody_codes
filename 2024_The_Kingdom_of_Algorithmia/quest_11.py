import numpy as np
from utils.input import readlines_input


def parse_input(part: int, start_termite: str | None):
    lines = [x.rstrip().split(":") for x in readlines_input(11, part)]
    all_termites = [x[0] for x in lines]
    t_len = len(all_termites)
    transformation = np.zeros((t_len, t_len), dtype=int)

    for line in lines:
        termite = line[0]
        products = line[1].split(",")
        for p in products:
            p_idx = all_termites.index(p)
            t_idx = all_termites.index(termite)
            transformation[p_idx][t_idx] += 1

    start = None
    if start_termite is not None:
        start = np.zeros((t_len, 1), dtype=int)
        start[all_termites.index(start_termite)] = 1
    return transformation, start


def solve(part, start_termite, days):
    transformation, start = parse_input(part, start_termite)
    transformation_after_n_days = np.linalg.matrix_power(transformation, days)
    return sum(transformation_after_n_days @ start)[0]


def main():
    print("Part 1:", solve(1, "A", 4))
    print("Part 2:", solve(2, "Z", 10))

    transformation, _ = parse_input(3, None)
    transformation_after_20_days = np.linalg.matrix_power(transformation, 20)
    result = np.sum(transformation_after_20_days, axis=0)
    print("Part 3:", max(result) - min(result))


if __name__ == "__main__":
    main()
