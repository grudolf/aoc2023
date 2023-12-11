import itertools
import logging


def calculate_distance(a, b):
    dist_x = abs(a[0] - b[0])
    dist_y = abs(a[1] - b[1])
    #logging.debug("Distance %s - %s: %s+%s", a, b, dist_x, dist_y)
    return dist_x + dist_y


def calculate_total_distance(galaxies):
    total_distance = 0
    for a, b in itertools.combinations(galaxies, 2):
        total_distance += calculate_distance(a, b)
    return total_distance


def row_is_empty(line):
    return all(c == '.' for c in line)


def get_galaxies(lines, grow):
    galaxies = []

    # find empty cols
    empty_cols = set()
    j = 0
    for i in range(len(lines[0])):
        empty = True
        for row in lines:
            if row[i] == '#':
                empty = False
                break
        if empty:
            empty_cols.add(j)
            j += grow
        j += 1
    logging.debug(sorted(empty_cols))

    row = 0
    for line in lines:
        if row_is_empty(line):
            row += grow + 1
            continue
        col = 0
        for v in line:
            if col in empty_cols:
                col += grow 
            else:
                if v == '#':
                    galaxies.append((row, col))
            col += 1
        row += 1
    logging.info(galaxies)
    return galaxies


def test1():
    lines = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split('\n')

    galaxies = get_galaxies(lines, 1)
    print(calculate_distance((0, 4), (10, 9)) == 15)
    result = calculate_total_distance(galaxies)
    print("Part 1", 374 == result, result)
    result = calculate_total_distance(get_galaxies(lines, 9))
    print("Part 2 (10)", 1030 == result, result)
    result = calculate_total_distance(get_galaxies(lines, 99))
    print("Part 2 (100)", 8410 == result, result)


def main():
    with open('aoc2023_day11.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    galaxies = get_galaxies(lines, 1)
    result = calculate_total_distance(galaxies)
    print("Part 1", result)
    result = calculate_total_distance(get_galaxies(lines, 999999))
    print("Part 2", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
