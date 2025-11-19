from functools import cmp_to_key


def get_swords(part: int):
    with open(f"input_{part}.txt") as f:
        return list(map(parse_sword, f.readlines()))


def parse_sword(sword_string):
    sword_id, tail = sword_string.split(":")
    return Sword(int(sword_id), list(map(int, tail.split(","))))


class Fishbone:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None
        self.next = None

    def insert(self, n: int):
        if self.value is None:
            self.value = n
        elif n < self.value and self.left is None:
            self.left = n
        elif n > self.value and self.right is None:
            self.right = n
        else:
            if self.next is None:
                self.next = Fishbone()
            self.next.insert(n)

    def level(self):
        l = "" if self.left is None else str(self.left)
        v = "" if self.value is None else str(self.value)
        r = "" if self.right is None else str(self.right)
        return int(l+v+r)

    def levels(self):
        if self.next is None:
            return [self.level()]
        return [self.level()] + self.next.levels()

    def quality(self):
        if self.next is None:
            return str(self.value)
        return str(self.value) + self.next.quality()

    def __str__(self):
        left = str(self.left) + "-" if self.left is not None else "  "
        right = "-" + str(self.right) if self.right is not None else "  "
        string = f"{left}{self.value}{right}"
        if self.next is not None:
            string += "\n" + str(self.next)
        return string


class Sword:
    def __init__(self, sword_id: int, sword_code: list[int]):
        self.id = sword_id
        self.fishbone = Fishbone()
        for n in sword_code:
            self.fishbone.insert(n)

    def quality(self):
        return int(self.fishbone.quality())


print("Part 1:", get_swords(1)[0].quality())

swords = get_swords(2)
sword_qualities = [sword.quality() for sword in swords]
print("Part 2:", max(sword_qualities) - min(sword_qualities))


def compare_swords(a: Sword, b: Sword):
    if a.quality() < b.quality():
        return -1
    if a.quality() > b.quality():
        return 1

    for al, bl in zip(a.fishbone.levels(), b.fishbone.levels()):
        if al == bl:
            continue
        if al < bl:
            return -1
        else:
            return 1

    return a.id - b.id


swords = sorted(get_swords(3), key=cmp_to_key(compare_swords), reverse=True)
print("Part 3:", sum(
    idx * sword for [idx, sword] in enumerate((sword.id for sword in swords), start=1)))
