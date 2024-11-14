def read_input(part: int):
    with open(f"/Users/trulshj/dev/everybody_codes/2024_The_Kingdom_of_Algorithmia/quest_04/part_{part}.txt") as f:
        return [int(line.rstrip()) for line in f.readlines()]


def find_strokes_to_even_nails(nails):
    shortest = min(nails)
    return sum(map(lambda x: x - shortest, nails))


def find_strokes_to_even_nails_2(nails):
    min_seen = float('inf')

    for target in range(min(nails), max(nails)):
        current = sum(map(lambda x, target=target: abs(x-target), nails))
        min_seen = min(min_seen, current)

    return min_seen


nails_1 = read_input(1)
print(find_strokes_to_even_nails(nails_1))

nails_2 = read_input(2)
print(find_strokes_to_even_nails(nails_2))

nails_3 = read_input(3)
print(find_strokes_to_even_nails_2(nails_3))
