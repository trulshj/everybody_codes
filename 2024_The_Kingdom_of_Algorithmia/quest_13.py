from utils.input import read_input, readlines_input
import numpy as np
import matplotlib.pyplot as plt


def parse_input(part: int):
    return [[(x[0], int(x[1:])) for x in line.rstrip().split(",")] for line in readlines_input(13, part)]


def find_final_height(instructions: list[tuple[str, int]]):
    max_height = 0
    height = 0
    for dir, amount in instructions:
        if dir == "U":
            height += amount
            if height > max_height:
                max_height = height
        elif dir == "D":
            height -= amount
    return max_height


def find_segments(instructions: list[tuple[str, int]]):
    xyz = np.array([0, 0, 0], dtype=int)
    segments = set()
    for dir, amount in instructions:
        match dir:
            case "U":
                delta = np.array([0, 1, 0], dtype=int)
            case "D":
                delta = np.array([0, -1, 0], dtype=int)
            case "L":
                delta = np.array([-1, 0, 0], dtype=int)
            case "R":
                delta = np.array([1, 0, 0], dtype=int)
            case "F":
                delta = np.array([0, 0, 1], dtype=int)
            case "B":
                delta = np.array([0, 0, -1], dtype=int)
        for _ in range(amount):
            xyz += delta
            segments.add(tuple(xyz))
    return segments, tuple(xyz)


def plot_plant(segments: set[tuple[int, int, int]], leaves: set[tuple[int, int, int]]):
    fig = plt.figure()
    segments -= leaves
    segments_xyz = list(zip(*segments))
    leaves_xyz = list(zip(*leaves))
    ax = fig.add_subplot(projection="3d")
    ax.scatter(*segments_xyz, c="tab:brown")
    ax.scatter(*leaves_xyz, c="green", marker="*")
    plt.show()


def main():
    plant = parse_input(1)[0]
    print("Part 1:", find_final_height(plant))

    plants = parse_input(2)
    segments = set()
    segments.update(*map(lambda x: find_segments(x)[0], plants))
    print(len(segments))

    tree = parse_input(3)
    leaves = set()
    segments = set()
    for branch in tree:
        branch_segments, leaf = find_segments(branch)
        segments.update(branch_segments)
        leaves.add(leaf)
    plot_plant(segments, leaves)


if __name__ == "__main__":
    main()
