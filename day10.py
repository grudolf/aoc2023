import logging


def find_start(tiles):
    for r, row in enumerate(tiles):
        for c, tile in enumerate(row):
            if tile[0] == 'S':
                return r, c
    return -1, -1


def part1(tiles):
    exits = {
        # symbol, allowed directions (exit to, entry from as NSEW)
        '|': [1, 1, 0, 0],
        '-': [0, 0, 1, 1],
        'L': [1, 0, 1, 0],
        'J': [1, 0, 0, 1],
        '7': [0, 1, 0, 1],
        'F': [0, 1, 1, 0],
        'S': [1, 1, 1, 1],
        '.': [0, 0, 0, 0]
    }
    r, c = find_start(tiles)
    logging.debug("Start at %s", (r, c))
    step = 1
    while 1:
        current_tile = tiles[r][c]
        moved = False
        for (target_r, target_c, out_dir, in_dir) in [[r - 1, c, 0, 1], [r, c + 1, 2, 3], [r + 1, c, 1, 0], [r, c - 1, 3, 2]]:
            if target_r < 0 or target_r >= len(tiles) or target_c < 0 or target_c >= len(tiles[0]):
                continue
            target_tile = tiles[target_r][target_c]
            if exits[current_tile[0]][out_dir] == 1 and exits[target_tile[0]][in_dir] == 1:
                if target_tile[1] > -1:
                    continue
                target_tile[1] = step
                step += 1
                logging.debug("Moved from %s to %s, direction %s", (r, c, current_tile),
                              (target_r, target_c, target_tile), out_dir)
                r, c = target_r, target_c
                moved = True
                break
        if not moved:
            break
    return int(step / 2)


def hor2vert(tile):
    if tile in ['|', 'L', 'J']:
        return True
    return False


def part2(tiles):
    inside_count = 0
    for l in tiles:
        row = ''
        inside = False
        for c in l:
            if c[1] >= 0:
                if hor2vert(c[0]):
                    inside = not inside
                    row += '|'
                else:
                    row += c[0]
            else:
                if inside:
                    c[0] = 'I'
                    inside_count += 1
                    row += 'I'
                else:
                    row += 'O'
        logging.info("%s %s", row, inside_count)
    return inside_count


def parse_input(lines):
    tiles = []
    for r in lines:
        tiles.append([[c, -1] for c in r])
    return tiles


def test1():
    lines = """.....
.S-7.
.|.|.
.L-J.
.....""".split('\n')
    tiles = parse_input(lines)
    result = part1(tiles)
    print("Part 1", 4 == result)

    lines = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...""".split('\n')
    tiles = parse_input(lines)
    result = part1(tiles)
    print("Part 1", 8 == result)


def test2():
    lines = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........""".split('\n')
    tiles = parse_input(lines)
    part1(tiles)
    result = part2(tiles)
    print("Part 2", 4 == result)
    lines = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".split('\n')
    tiles = parse_input(lines)
    part1(tiles)
    result = part2(tiles)
    print("Part 2", 10 == result)


def main():
    with open('aoc2023_day10.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    tiles = parse_input(lines)
    result = part1(tiles)
    print("Part 1", result)
    result = part2(tiles)
    print("Part 2", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    test2()
    main()
