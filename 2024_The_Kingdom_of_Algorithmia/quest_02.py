from utils.input import read_input


def parse_input(part):
    h, t = read_input(2, part).split("\n\n")
    words = h.split(":")[-1].split(",")
    inscriptions = [x.rstrip() for x in t.split()]
    return words, inscriptions


def part_1():
    words, inscriptions = parse_input(1)

    runic_words = 0
    for word in words:
        for inscription in inscriptions:
            if word in inscription:
                runic_words += 1

    return runic_words


def part_2():
    words, inscriptions = parse_input(2)
    words += list(map(lambda w: w[::-1], words))
    inscription = " ".join(inscriptions)
    runic_symbols = [False] * len(inscription)

    for i in range(0, len(inscription)):
        for word in words:
            if len(word) + i >= len(inscription):
                continue

            check = inscription[i:i+len(word)]
            if word == check or word[::-1] == check:
                for j in range(i, i+len(word)):
                    runic_symbols[j] = True

    return sum(runic_symbols)


def part_3():
    words, inscriptions = parse_input(3)
    words += list(map(lambda w: w[::-1], words))

    rows = len(inscriptions)
    cols = len(inscriptions[0])
    runic_symbols = [False] * (rows * cols)

    def update_symbols(coords):
        for c in coords:
            runic_symbols[c] = True

    def get_horizontal(word, x, y):
        coords = []

        for idx, c in enumerate(word):
            xn = (x+idx) % cols
            if c == inscriptions[y][xn]:
                coords.append(y * cols + xn)
            else:
                return []

        return coords

    def get_vertical(word, x, y):
        coords = []

        for idx, c in enumerate(word):
            yn = y+idx
            if c == inscriptions[yn][x]:
                coords.append(((yn) * cols) + x)
            else:
                return []

        return coords

    for y in range(rows):
        for x in range(cols):
            for word in words:
                coords = get_horizontal(word, x, y)
                update_symbols(coords)

                if (y+len(word) > rows):
                    continue

                coords = get_vertical(word, x, y)
                update_symbols(coords)

    return sum(runic_symbols)


print("Part 1:", part_1())
print("Part 2:", part_2())
print("Part 3:", part_3())
