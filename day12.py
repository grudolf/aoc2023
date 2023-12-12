import logging


def parse_input(lines):
    parsed = []
    for line in lines:
        l = line.split()
        springs = [c for c in l[0]]
        groups = [int(i) for i in l[1].split(',')]
        parsed.append((springs, groups))
    return parsed


def calc_scores(springs, pos):
    scores = []
    score = 0
    for c in springs[:pos]:
        if c == '.':
            if score > 0:
                scores.append(score)
                score = 0
        elif c == '#':
            score += 1
    if score:
        scores.append(score)
    return scores


def get_arrangement(springs, groups, pos):
    logging.debug((springs, pos))

    # calc score so far
    scores = calc_scores(springs, pos)
    for s, g in zip(scores, groups):
        if s > g:
            logging.debug("Calculated scores too big: %s - %s", scores, groups)
            return 0
    if pos == len(springs):
        if len(scores) == len(groups) and all(s == g for s, g in zip(scores, groups)):
            logging.info("Match " + ''.join(springs))
            return 1
        else:
            logging.debug("No match " + ''.join(springs))
            return 0

    while pos < len(springs):
        if springs[pos] == '?':
            tot = 0
            springs[pos] = '#'
            tot = tot + get_arrangement(springs, groups, pos + 1)
            springs[pos] = '.'
            tot = tot + get_arrangement(springs, groups, pos + 1)
            springs[pos] = '?'
            return tot
        pos += 1
    return get_arrangement(springs, groups, pos)


def part1(rows):
    total = 0
    for springs, groups in rows:
        logging.info((springs, groups))
        score = get_arrangement(springs, groups, 0)
        logging.info(score)
        total += score
    return total


def test1():
    lines = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split('\n')
    result = part1(parse_input(lines))
    print("Part 1", 21 == result, result)


def main():
    with open('aoc2023_day12.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    result = part1(parse_input(lines))
    print("Part 1", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test1()
    main()
