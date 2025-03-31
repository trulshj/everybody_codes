from utils.input import readlines_input
from itertools import permutations


def parse_input(part):
    f = [l.rstrip().split(':') for l in readlines_input(7, part)]
    return [(x[0], x[1].split(',')) for x in f]


def run_plan(plan, rounds=10):
    power = 10
    magical_essence = 0
    for i in range(rounds):
        action = plan[1][i % len(plan[1])]
        match action:
            case '+':
                power += 1
            case '-':
                power -= 1
        magical_essence += power
    return (plan[0], magical_essence)


def part_1():
    plans = parse_input(1)
    plan_results = map(run_plan, plans)
    sorted_plans = sorted(plan_results, key=lambda x: x[1], reverse=True)
    print("".join(map(lambda x: x[0], sorted_plans)))


def run_plan_on_track(plan, track, loops=10):
    power = 10
    magical_essence = 0
    current_loop = 0
    i = 0

    while current_loop < loops:
        action = plan[1][i % len(plan[1])]
        track_action = track[(i) % len(track)]

        if track_action == 'S':
            current_loop += 1

        if track_action == '+':
            power += 1
        elif track_action == '-':
            power -= 1
        else:
            match action:
                case '+':
                    power += 1
                case '-':
                    power -= 1

        magical_essence += power
        i += 1

    return (plan[0], magical_essence)


def part_2():
    TRACK = "-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=---=++==--+++==++=+=--==++==+++=++=+++=--=+=-=+=-+=-+=-+-=+=-=+=-+++=+==++++==---=+=+=-S"

    plans = parse_input(2)
    plan_results = map(lambda plan: run_plan_on_track(plan, TRACK), plans)
    sorted_plans = sorted(plan_results, key=lambda x: x[1], reverse=True)
    print(sorted_plans)
    print("".join(map(lambda x: x[0], sorted_plans)))


def part_3():
    OPPONENT_PLAN = ("A", "=,-,+,+,=,+,-,=,+,+,-".split(","))

    track_grid = [line.rstrip('\n') for line in readlines_input(7, 3)]

    print()
    for l in track_grid:
        print(f"'{l}'")
    print()

    visited = set()
    stack = [(0, 1)]
    deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    track = ""
    max_y = len(track_grid)
    max_x = len(track_grid[0])

    while stack:
        y, x = stack.pop()
        if (y, x) in visited:
            continue

        track += track_grid[y][x]

        visited.add((y, x))

        for dy, dx in deltas:
            ny = y + dy
            nx = x + dx

            if nx < 0 or ny < 0:
                continue

            if nx >= max_x or ny >= max_y:
                continue

            if (ny, nx) not in visited and track_grid[ny][nx] != ' ':
                stack.append((ny, nx))
                break

    RESULT_TO_BEAT = run_plan_on_track(OPPONENT_PLAN, track, 2024)
    print(RESULT_TO_BEAT)

    available_actions = "+++++---==="
    all_plans = set(permutations(available_actions, 11))
    total = len(all_plans)

    winning_plans = 0

    for idx, plan in enumerate(all_plans):
        p = ('X', plan)
        r = run_plan_on_track(p, track, 2024)
        if r[1] > RESULT_TO_BEAT[1]:
            winning_plans += 1
        print(f"Winning plans: {winning_plans}, Progress: {
            idx}/{total} - {round(idx * 100 / total, 2)}%, Current Plan Score: {r[1]}, Score to Beat: {RESULT_TO_BEAT[1]}")

    print(winning_plans)


part_3()
