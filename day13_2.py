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


def count_mismatches(row1, row2):
    return len([r1+r2 for r1, r2 in zip(row1, row2) if r1!=r2])


def check_rows_with_smudges(pattern, smudges):
    """
    Instead of checking for identical mirrored rows we try to find mirrored rows with exactly x differences/smudges:
    - 0 for part 1 - all identical
    - 1 smudge for part 2

    Optimistic approach at first - find first/unique solution with 1 smudge, without checking if smudge is in the same place when rotated
    """
    results = []
    for start in range(0, len(pattern)-1):
        logging.debug("Start at %s", start)
        i, j = start, start + 1
        mismatches = 0
        while i >= 0 and j < len(pattern):
            mismatches += count_mismatches(pattern[i], pattern[j])
            i -= 1
            j += 1
        if mismatches == smudges:
            logging.debug("%s Smudged mirror after line %s", start, start + 1)
            results.append(start + 1)
            return start+1
    if not results:
        return 0
    if len(results)==1:
        return results[0]
    raise ValueError(f"Single result expected, pattern={pattern}, results={results}")


def check_pattern(pattern):
    return 100 * check_rows(pattern) + check_rows(rotate(pattern))

def check_smudged_pattern(pattern, smudges):
    return 100 * check_rows_with_smudges(pattern, smudges) + check_rows_with_smudges(rotate(pattern), smudges)


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


def check_smudged_patterns(patterns, smudges):
    results = []
    for pattern in patterns:
        results.append(check_smudged_pattern(pattern, smudges))
    return sum(results)


def test1():
    print("Rotation check: ", ["IEA", "JFB", "KGC", "LHD"] == rotate(["ABCD", "EFGH", "IJKL"]))
    print("Mismatch check: ", 2==count_mismatches("abcd", "adcb"))

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
    print(5 == check_smudged_pattern(patterns[0], 0))
    print(400 == check_smudged_pattern(patterns[1], 0))

    print(300 == check_smudged_pattern(patterns[0], 1))
    print(100 == check_smudged_pattern(patterns[1], 1))


def main():
    with open('aoc2023_day13.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    patterns = parse_patterns(lines)
    print("Part 1", check_patterns(patterns))
    print("Part 1", check_smudged_patterns(patterns, 0))
    print("Part 2", check_smudged_patterns(patterns, 1))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test1()
    main()
