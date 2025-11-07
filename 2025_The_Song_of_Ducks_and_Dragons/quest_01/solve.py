
def read_input(part: int):
    with open(f"input_{part}.txt", "r") as f:
        names, instructions = f.read().split()
        names = names.split(",")
        instructions = instructions.split(",")
        print(names, instructions)
    return names, instructions


def find_linear_name(names, instructions):
    index = 0
    for instruction in instructions:
        if instruction[0] == 'R':
            index = min(index + int(instruction[1]), len(names) - 1)
        else:
            index = max(index - int(instruction[1]), 0)
    return names[index]


def find_circular_name(names, instructions):
    index = 0
    for instruction in instructions:
        if instruction[0] == 'R':
            index += int(instruction[1:])
        else:
            index -= int(instruction[1:])
    return names[index % len(names)]


def find_swap_name(names, instructions):
    for instruction in instructions:
        if instruction[0] == 'R':
            index = int(instruction[1:]) % len(names)
            names[0], names[index] = names[index], names[0]
        else:
            index = (-int(instruction[1:])) % len(names)
            names[0], names[index] = names[index], names[0]
    return names[0]


def part1():
    return find_linear_name(*read_input(1))


def part2():
    return find_circular_name(*read_input(2))


def part3():
    return find_swap_name(*read_input(3))


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())
    print("Part 3:", part3())


if __name__ == "__main__":
    main()
