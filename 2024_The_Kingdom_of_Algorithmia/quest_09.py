from utils.input import read_input


def parse_input(part: int):
    return [int(x) for x in read_input(9, part).split()]


def precompute_min_stamps(stamps, max_sparkball):
    dp = [float('inf')] * (max_sparkball + 1)
    dp[0] = 0
    for stamp in stamps:
        for j in range(stamp, max_sparkball + 1):
            dp[j] = min(dp[j], dp[j - stamp] + 1)
    return dp


def calc_min_split_beetles(stamps, sparkballs):
    beetle_count = 0
    dp = precompute_min_stamps(stamps, max(sparkballs))

    for ball in sparkballs:
        min_count = float('inf')

        for target in range(max(0, ball // 2 - 100), min(ball, ball // 2 + 101)):
            other = ball - target
            if abs(target - other) > 100:
                continue

            min_1 = dp[target]
            min_2 = dp[ball-target]
            count = min_1 + min_2
            if count < min_count:
                min_count = count

        beetle_count += min_count

    return beetle_count


def main():

    def solve(stamps, sparkballs):
        dp = precompute_min_stamps(stamps, max(sparkballs))
        return sum(map(lambda x: dp[x], sparkballs))

    stamps_1 = (1, 3, 5, 10)
    sparkballs_1 = parse_input(1)
    print("Part 1:", solve(stamps_1, sparkballs_1))

    stamps_2 = (1, 3, 5, 10, 15, 16, 20, 24, 25, 30)
    sparkballs_2 = parse_input(2)
    print("Part 2:", solve(stamps_2, sparkballs_2))

    stamps_3 = (1, 3, 5, 10, 15, 16, 20, 24, 25,
                30, 37, 38, 49, 50, 74, 75, 100, 101)
    sparkballs_3 = parse_input(3)
    s_3 = calc_min_split_beetles(stamps_3, sparkballs_3)
    print("Part 3:", s_3)


if __name__ == "__main__":
    main()
