from math import trunc

type Complex = tuple[int, int]


def add(a: Complex, b: Complex) -> Complex:
    return (a[0] + b[0], a[1] + b[1])


def mul(a: Complex, b: Complex) -> Complex:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def div(a: Complex, b: Complex) -> Complex:
    return (trunc(a[0] / b[0]), trunc(a[1] / b[1]))


def calibrate(a: Complex):
    result = (0, 0)
    for _ in range(3):
        result = mul(result, result)
        result = div(result, (10, 10))
        result = add(result, a)
    return result


def get_grid_points(initial: Complex):
    for y in range(101):
        for x in range(101):
            yield add(initial, (x*10, y*10))


def get_detailed_grid_points(initial: Complex):
    for y in range(1001):
        for x in range(1001):
            yield add(initial, (x, y))


def point_is_within_bounds(point: Complex):
    return abs(point[0]) <= 1_000_000 and abs(point[1]) <= 1_000_000


def engrave_point(point: Complex):
    result = (0, 0)
    for _ in range(1, 101):
        result = mul(result, result)
        result = div(result, (100_000, 100_000))
        result = add(result, point)
        if not point_is_within_bounds(result):
            return False
    return True


def engrave_points(initial: Complex):
    return map(engrave_point, get_grid_points(initial))


def engrave_detailed_points(initial: Complex):
    return map(engrave_point, get_detailed_grid_points(initial))


def draw_design(design):
    for y in range(101):
        for x in range(101):
            print('x' if design[x + 101*y] else '·', end='')
        print()


def main():
    A: Complex = (152, 57)
    result = calibrate(A)
    print(f"Part 1: [{result[0]},{result[1]}]")

    initial_design_corner = (-79745, -16616)
    design = list(engrave_points(initial_design_corner))

    # draw_design(design)

    print(f"Part 2: {sum(design)}")

    detailed_design = engrave_detailed_points(initial_design_corner)

    print(f"Part 3: {sum(detailed_design)}")


if __name__ == "__main__":
    main()
