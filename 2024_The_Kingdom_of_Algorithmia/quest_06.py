from utils.input import read_input
from collections import deque, Counter, defaultdict


def parse_input(part):
    lines = [l.split(':') for l in read_input(6, part).split()]
    graph = defaultdict(list, {x[0]: x[1].split(',') for x in lines})
    return graph


def bfs(graph):
    queue = deque([("RR", [], 0)])
    visited = set()
    paths = []
    while queue:
        node, path, depth = queue.popleft()
        visited.add(node)

        leaves = graph[node]
        for leaf in leaves:
            if leaf == "@":
                paths.append((path + [node, leaf], depth+2))
                continue
            if leaf in visited:
                continue
            queue.append((leaf, path + [node], depth + 1))

    return paths


def find_longest_path(part):
    graph = parse_input(part)
    paths = bfs(graph)
    depth_counts = Counter(map(lambda x: x[1], paths))

    for k, v in depth_counts.items():
        if v == 1:
            distinct_length = k

    for path in paths:
        if path[1] == distinct_length:
            if part == 1:
                print("".join(path[0]))
            else:
                print("".join(map(lambda x: x[0], path[0])))
            break


if __name__ == "__main__":
    find_longest_path(1)
    find_longest_path(2)
    find_longest_path(3)
