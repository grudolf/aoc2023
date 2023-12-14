import logging


def parse_input(lines):
    return [list(l) for l in lines]


def tilt_north(platform):
    for col in range(0, len(platform[0])):
        while True:
            moved = False
            for row in range(0, len(platform)-1):
                if platform[row][col]=='.' and platform[row+1][col]=='O':
                    platform[row][col]='O'
                    platform[row+1][col]='.'
                    moved = True
            if not moved:
                break


def load_when_tilted_north(platform):
    total = 0
    h = len(platform)
    for row in range(0, h):
        dist = h - row
        rocks = len([c for c in platform[row] if c=='O'])
        load = dist * rocks
        logging.info("%s : %d %d", ''.join(platform[row]), dist, rocks)
        total += load
    return total


def display(platform):
    logging.info('')
    for r in platform:
        logging.info(''.join(r))


def test1():
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
    print(136 == load)


def main():
    with open('aoc2023_day14.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    platform = parse_input(lines)
    display(platform)
    tilt_north(platform)
    display(platform)
    load = load_when_tilted_north(platform)
    print("Part 1:", load)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
