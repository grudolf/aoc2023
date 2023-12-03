import logging
from functools import reduce


def parse_input(lines: list[str]):
    symbols = []
    part_numbers = []
    for r, line in enumerate(lines):
        part_number = ''
        part_number_c = 0
        for c, char in enumerate(line + '.'):
            if char.isdigit():
                if part_number == '':
                    part_number_c = c
                part_number += char
                continue
            if part_number:
                part_numbers.append({'r': r, 'c': part_number_c, 'part_number': part_number})
                part_number = ''
            if char != '.':
                symbols.append({'r': r, 'c': c, 'symbol': char, 'part_numbers': []})
    logging.debug(symbols)
    logging.debug(part_numbers)
    return symbols, part_numbers


def find_valid_part_numbers(symbols, part_numbers):
    results = []
    for part_number in part_numbers:
        r = part_number['r']
        c = part_number['c']
        l = len(part_number['part_number'])
        # row +- 1 and max 1 col away from start or end of part number
        # part 1
        # if any(abs(r - s['r']) < 2 and c - 1 <= s['c'] <= c + l for s in symbols):
        #     results.append(part_number)
        # part 2: additionally link part numbers to each symbol
        adjacent = False
        for symbol in (s for s in symbols if abs(r - s['r']) < 2 and c - 1 <= s['c'] <= c + l):
            adjacent = True
            symbol['part_numbers'].append(part_number)
        if adjacent:
            results.append(part_number)
    return results


def calculate_gear_ratio(symbols):
    total = 0
    for s in symbols:
        if s['symbol'] != '*':
            continue
        if len(s['part_numbers']) == 2:
            gear_ratio = int(s['part_numbers'][0]['part_number']) * int(s['part_numbers'][1]['part_number'])
            total += gear_ratio
    return total


def test1():
    lines = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split('\n')
    symbols, part_numbers = parse_input(lines)
    valid_part_numbers = find_valid_part_numbers(symbols, part_numbers)
    result = reduce(lambda a, b: a + b, [int(p['part_number']) for p in valid_part_numbers])
    print("Part 1", 4361 == result)
    print("Part 2", 467835 == calculate_gear_ratio(symbols))


def main():
    with open('aoc2023_day03.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    symbols, part_numbers = parse_input(lines)
    valid_part_numbers = find_valid_part_numbers(symbols, part_numbers)
    result = reduce(lambda a, b: a + b, [int(p['part_number']) for p in valid_part_numbers])
    print("Part 1", result)
    print("Part 2", calculate_gear_ratio(symbols))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
