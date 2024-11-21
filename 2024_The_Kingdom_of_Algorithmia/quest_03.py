from collections import defaultdict
from utils.input import readlines_input


def parse_input(part: int):
    return [line.rstrip() for line in readlines_input(3, part)]


def pad_grid(grid):
    for idx, row in enumerate(grid):
        grid[idx] = f".{row}."

    grid.insert(0, '.' * len(grid[0]))
    grid.append('.' * len(grid[0]))


def get_neighbours(grid, row, col, include_diagonals=False):
    ORTHOGONALS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    DIAGONALS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    OFFSETS = ORTHOGONALS
    if include_diagonals:
        OFFSETS += DIAGONALS

    nhs = []
    for dy, dx in OFFSETS:
        nx = col + dx
        ny = row + dy
        if ny >= len(grid) or ny < 0 or nx < 0 or nx >= len(grid[0]):
            continue
        nhs.append((ny, nx))
    return nhs


def depth_difference(depths, k, n, threshold=1):
    kd = depths[k] + 1
    nd = depths[n]
    return abs(kd - nd) <= threshold


def dig_grid(grid, include_diagonals=False):
    graph = {}
    depths = defaultdict(int)
    nodes = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            graph[(row, col)] = get_neighbours(
                grid, row, col, include_diagonals)
            if grid[row][col] == '#':
                nodes.append((row, col))

    digs = 0
    old_digs = None

    while digs != old_digs:
        old_digs = digs
        for k in nodes:
            if all(map(lambda n, k=k: depth_difference(depths, k, n), graph[k])):
                depths[k] += 1
                digs += 1

    return digs


grid_1 = parse_input(1)
print(dig_grid(grid_1))

grid_2 = parse_input(2)
print(dig_grid(grid_2))

grid_3 = parse_input(3)
pad_grid(grid_3)
print(dig_grid(grid_3, include_diagonals=True))
