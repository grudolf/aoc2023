import logging


def part1(lines: list[str]) -> int:
    total = 0
    for line in lines:
        first_digit = next(x for x in line if x.isdigit())
        last_digit = next(x for x in reversed(line) if x.isdigit())
        logging.debug("%s -> %s%s", line, first_digit, last_digit)
        total += int(first_digit + last_digit)
    return total


def part2(lines: list[str]) -> int:
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    for line in lines:
        numbers = []
        for idx, char in enumerate(line):
            if char.isdigit():
                numbers.append(char)
            else:
                for word in words:
                    if line[idx:].startswith(word):
                        numbers.append(str(words.index(word) + 1))
        first_digit = numbers[0]
        last_digit = numbers[-1]
        logging.debug("%s -> %s -> %s%s", line, numbers, first_digit, last_digit)
        total += int(first_digit + last_digit)
    return total


def test1():
    lines = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split('\n')
    result = part1(lines)
    print("Part 1", 142 == result)

    lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split('\n')
    result = part2(lines)
    print("Part 2", 281 == result)


def main():
    with open('aoc2023_day01.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    print("Part 1", part1(lines))
    print("Part 2", part2(lines))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
