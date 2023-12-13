import logging


def parse_patterns(lines):
    patterns = []
    pattern = []
    for line in lines:
        if line:
            pattern.append(line)
        else:
            patterns.append(pattern)
            pattern = []
    patterns.append(pattern)
    return patterns


def check_rows(pattern):
    for start in range(0, len(pattern)-1):
        logging.info("Start at %s", start)
        i, j = start, start + 1
        mirror = True
        while i >= 0 and j < len(pattern):
            if pattern[i] != pattern[j]:
                logging.debug("%s Mismatch at %d %d: %s %s", start, i, j, pattern[i], pattern[j])
                mirror = False
                break
            logging.debug("%s Match at %d %d: %s %s", start, i, j, pattern[i], pattern[j])
            i -= 1
            j += 1
        if mirror:
            logging.info("%s Mirror after line %s", start, start + 1)
            return start+1
    return 0


def check_pattern(pattern):
    return 100 * check_rows(pattern) + check_rows(rotate(pattern))


def rotate(pattern):
    """
    Rotate pattern 90 deg right
    :param pattern:
    ABCD
    EFGH
    IJKL

    :return:
    IEA
    JFB
    KGC
    LHD
    """
    result = [''.join(reversed(a)) for a in zip(*pattern)]
    return result


def check_patterns(patterns):
    results = []
    for pattern in patterns:
        results.append(check_pattern(pattern))
    return sum(results)


def test1():
    print("Rotation check: ", ["IEA", "JFB", "KGC", "LHD"] == rotate(["ABCD", "EFGH", "IJKL"]))

    lines = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split('\n')
    patterns = parse_patterns(lines)
    logging.info(patterns)
    print(5 == check_pattern(patterns[0]))
    print(400 == check_pattern(patterns[1]))
    print(405 == check_patterns(patterns))


def main():
    with open('aoc2023_day13.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    patterns = parse_patterns(lines)
    print("Part 1", check_patterns(patterns))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
