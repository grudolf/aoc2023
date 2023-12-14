import logging


def parse_input(lines):
    return [list(l) for l in lines]


def tilt_north(platform):
    for col in range(0, len(platform[0])):
        while True:
            moved = False
            for row in range(0, len(platform) - 1):
                if platform[row][col] == '.' and platform[row + 1][col] == 'O':
                    platform[row][col] = 'O'
                    platform[row + 1][col] = '.'
                    moved = True
            if not moved:
                break


def load_when_tilted_north(platform):
    total = 0
    h = len(platform)
    for row in range(0, h):
        dist = h - row
        rocks = len([c for c in platform[row] if c == 'O'])
        load = dist * rocks
        logging.debug("%s : %d %d", ''.join(platform[row]), dist, rocks)
        total += load
    return total


def display(platform):
    logging.info('')
    for r in platform:
        logging.info(''.join(r))


def rotate_left(platform):
    """
    rotate left / anti-clockwise
    :param platform:
    123
    456
    789
    :return:
    369
    258
    147
    """
    rotated = [list(r) for r in list(zip(*platform))[::-1]]
    return rotated


def rotate_right(platform):
    """
    rotate right / clockwise
    :param platform:
    123
    456
    789
    :return:
    741
    852
    963
    """
    rotated = [list(r) for r in zip(*platform[::-1])]
    return rotated


def cycle(platform):
    # cycle
    # N
    tilt_north(platform)
    # W
    platform = rotate_right(platform)
    tilt_north(platform)
    # S
    platform = rotate_right(platform)
    tilt_north(platform)
    # E
    platform = rotate_right(platform)
    tilt_north(platform)

    platform = rotate_right(platform)
    return platform


def hashed(platform):
    result = ''.join(i for row in platform for i in row)
    return hash(result)


def part2(platform):
    hashes = {}
    i = 0
    target_cycle = 1000000000
    first = 0
    cycle_size = 0
    while i < target_cycle:
        platform = cycle(platform)
        platform_hash = hashed(platform)
        use_count = hashes.get(platform_hash, 0) + 1
        hashes[platform_hash] = use_count
        i += 1
        if use_count > 1:
            logging.debug("Cycles %d, known platform configurations: %d, %s seen %d time", i, len(hashes), platform_hash, use_count)
        # calculate repeating cycle size, at 10th iteration it should be stable
        if use_count == 10 and first == 0:
            first = i
            logging.info("Cycle %d, first 10", i)
        elif use_count == 11 and cycle_size == 0:
            cycle_size = i - first
            logging.info("Cycle %d, first 11, cycle size %d", i, cycle_size)
            x = int((target_cycle - i) / cycle_size) * cycle_size
            i = i + x
            logging.info("Skipping %d cycles to %d", x, i)
        if target_cycle - i < cycle_size:
            load = load_when_tilted_north(platform)
            logging.info("%d load %d", i, load)
    load = load_when_tilted_north(platform)
    return load


def test1():
    print("Left: ", rotate_left([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print("Right: ", rotate_right([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    lines = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".split('\n')
    platform = parse_input(lines)
    display(platform)
    tilt_north(platform)
    display(platform)
    load = load_when_tilted_north(platform)
    print("Test1: ", 136 == load)

    logging.info("Test2")
    platform = parse_input(lines)
    display(platform)

    # eh, no go, much too much
    # for i in range(0, 1000000000):
    #     platform = cycle(platform)
    #     if i % 1==0:
    #         load = load_when_tilted_north(platform)
    #         logging.info("%d: %d", i, load)

    print("Test2: ", 64 == part2(platform))


def main():
    with open('aoc2023_day14.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    platform = parse_input(lines)
    display(platform)
    tilt_north(platform)
    display(platform)
    load = load_when_tilted_north(platform)
    print("Part 1:", load)

    platform = parse_input(lines)
    display(platform)
    print("Part 2:", part2(platform))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # test1()
    main()
