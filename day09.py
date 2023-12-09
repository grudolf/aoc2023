import logging


def calc_history(seq):
    right = 0
    first = []
    while len(seq)>0:
        newseq = []
        first.append(seq[0])
        right += seq[-1]
        logging.debug(" %s - %s", seq, right)
        for t in zip(seq, seq[1:]):
            #logging.debug(t)
            newseq.append(t[1]-t[0])
        seq = newseq
        if all(v == 0 for v in seq):
            break
    left = 0
    #logging.debug(first)
    first.reverse()
    for i in first:
        # logging.debug("%s  %s",i-left,  left)
        # logging.debug("  %s",i)
        left = i - left
    # logging.debug("final %s",left)
    return left, right


def part1(lines):
    total_left = 0
    total_right = 0
    for line in lines:
        seq = [int(i) for i in line.split()]
        left, right = calc_history(seq)
        logging.info("%s | %s | %s", left, line, right)
        total_left += left
        total_right += right
    return total_left, total_right
        

def test1():
    lines = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".split('\n')
    l,r = part1(lines)
    print("Part 1", 114 == r)
    print("Part 2", 2 == l)


def main():
    with open('aoc2023_day09.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    l,r = part1(lines)
    print("Part 1", r)
    print("Part 2", l)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test1()
    main()
