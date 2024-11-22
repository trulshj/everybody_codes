from utils.input import readlines_input


def parse_input(part: int):
    return [int(line.rstrip()) for line in readlines_input(4, part)]


def find_strokes_to_even_nails(nails):
    shortest = min(nails)
    return sum(map(lambda x: x - shortest, nails))


# Thanks to Jakob, aka The Baron, Big Genius
def find_strokes_using_median(nails):
    median_idx = len(nails) // 2
    median = sorted(nails)[median_idx]
    
    return sum(map(lambda x: abs(x - median), nails))


if __name__ == "__main__":
    nails_1 = parse_input(1)
    print(find_strokes_to_even_nails(nails_1))

    nails_2 = parse_input(2)
    print(find_strokes_to_even_nails(nails_2))

    nails_3 = parse_input(3)
    print(find_strokes_using_median(nails_3))
