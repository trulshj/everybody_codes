
def read_input(part):
    with open(f"part_{part}.txt") as f:
        h, t = f.read().split("\n\n")
        words = h.split(":")[-1].split(",")
        inscriptions = [x.rstrip() for x in t.split()]
    return words, inscriptions


def part_1():
    words, inscriptions = read_input(1)

    runic_words = 0
    for word in words:
        for inscription in inscriptions:
            if word in inscription:
                runic_words += 1

    print(runic_words)


def part_2():
    words, inscriptions = read_input(2)
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

    print(sum(runic_symbols))


def part_3():
    words, inscriptions = read_input(3)
    print(words)
    print(inscriptions)

    rows = len(inscriptions)
    cols = len(inscriptions[0])

    runic_symbols = [False] * (rows * cols)

    for y in range(rows):
        for x in range(cols):
            for word in words:
                if (x+len(word) > cols) or (y+len(word) > rows):
                    continue
                left = ""
                down = ""

                i = x + (y * cols)

                if (x+len(word) <= cols):
                    left = ""
                    for l in range(len(word)):
                        left += inscriptions[y][x+l]
                    print(left)
                    if left == word or left == word[::-1]:
                        runic_symbols[i] = True

                if (y+len(word) <= rows):
                    down = ""
                    for l in range(len(word)):
                        down += inscriptions[y+l][x]
                    if down == word or down == word[::-1]:
                        runic_symbols[i] = True

    print(sum(runic_symbols))


part_3()
