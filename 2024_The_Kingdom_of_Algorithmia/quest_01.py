
potions_per_enemy = {
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 5,
    'x': 0
}


def calculate_potions(enemies):
    potions = 0
    for enemy in enemies:
        potions += potions_per_enemy[enemy]
    return potions


def calculate_potions_on_pairs(enemies):
    potions = 0

    for i in range(0, len(enemies), 2):
        e1 = enemies[i]
        e2 = enemies[i+1]
        potions += potions_per_enemy[e1]
        potions += potions_per_enemy[e2]
        if (e1 != 'x' and e2 != 'x'):
            potions += 2

    return potions


def calculate_potions_on_threes(enemies):
    potions = 0

    for i in range(0, len(enemies), 3):
        e1 = enemies[i]
        e2 = enemies[i+1]
        e3 = enemies[i+2]

        potions += potions_per_enemy[e1]
        potions += potions_per_enemy[e2]
        potions += potions_per_enemy[e3]

        e_count = sum(map(lambda x: x != 'x', [e1, e2, e3]))

        if e_count == 3:
            potions += 6
        elif e_count == 2:
            potions += 2

    return potions


PART_1_TEST_INPUT = "ABBAC"
PART_2_TEST_INPUT = "AxBCDDCAxD"
PART_3_TEST_INPUT = "xBxAAABCDxCC"

with open('part_1.txt') as f:
    enemies = f.readline().rstrip()

print(calculate_potions(enemies))

with open('part_2.txt') as f:
    enemies2 = f.readline().rstrip()

print(calculate_potions_on_pairs(PART_2_TEST_INPUT))
print(calculate_potions_on_pairs(enemies2))

with open('part_3.txt') as f:
    enemies3 = f.readline().rstrip()

print(calculate_potions_on_threes(PART_3_TEST_INPUT))
print(calculate_potions_on_threes(enemies3))
