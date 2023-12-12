import logging
from functools import cache


def parse_input2(lines):
    parsed = []
    for line in lines:
        l = line.split()
        springs = '?'.join([l[0]] * 5)
        groups = tuple(int(i) for i in l[1].split(',') * 5)
        parsed.append((springs, groups))
    return parsed


def parse_input(lines):
    parsed = []
    for line in lines:
        l = line.split()
        springs = l[0]
        groups = tuple(int(i) for i in l[1].split(','))
        parsed.append((springs, groups))
    return parsed


@cache
def get_arrangement_count(springs, groups) -> int:
    """ Move through springs and groups, check group size validity ASAP
        and either give up quickly or proceed with a smaller problem. """
    #logging.debug((springs, groups))

    char = springs[0] if springs else ''
    if char == '':
        # nothing else to do, success if groups are empty
        return 1 if len(groups) == 0 else 0

    if char == '?':
        # operational/damaged branches
        return get_arrangement_count('.' + springs[1:], groups) + get_arrangement_count('#' + springs[1:], groups)
    if char == '.':
        # operational, with remaining springs
        return get_arrangement_count(springs[1:], groups)
    if char == '#':
        # damaged
        if len(groups) == 0:
            # ended too soon
            return 0
        group_size = groups[0]
        # verify that none of the springs in the group is operational
        group_content = springs[:group_size]
        if '.' in group_content or len(group_content) != group_size:
            return 0
        if len(springs) == group_size and len(groups) == 1:
            # last group and the size matches with remaining springs
            logging.debug("Matched %s with %s", springs, groups)
            return 1
        if len(springs) > group_size:
            # check next spring
            if springs[group_size] == '#':
                # more damaged springs than requested
                return 0
            if springs[group_size] == '?':
                # skip, mark next spring as operational and repeat
                return get_arrangement_count('.' + springs[group_size + 1:], groups[1:])
        # skip and repeat
        #logging.debug("Accepting (%s)%s", springs[:group_size], springs[group_size:])
        return get_arrangement_count(springs[group_size:], groups[1:])
    return 0


def count_arrangements(rows):
    scores = []
    for springs, groups in rows:
        score = get_arrangement_count(springs, groups)
        scores.append(score)
        logging.info((springs, groups, score))
        #logging.debug(get_arrangement_count.cache_info())
        get_arrangement_count.cache_clear()
    logging.info(scores)
    return sum(scores)


def test1():
    lines = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split('\n')
    result = count_arrangements(parse_input(lines))
    print("Part 1", 21 == result, result)  # 1, 4, 1, 1, 4, 10
    result = count_arrangements(parse_input2(lines))
    print("Part 1", 525152 == result, result)  # 1, 16384, 1, 16, 2500, 506250


def main():
    with open('aoc2023_day12.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    result = count_arrangements(parse_input(lines))
    print("Part 1", result)
    result = count_arrangements(parse_input2(lines))
    print("Part 2", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test1()
    main()
