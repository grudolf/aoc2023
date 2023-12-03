import logging
import re


def sum_calibration_values(lines):
    total = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if digits:
            total += int(digits[0] + digits[-1])

    return total


def sum_calibration_values_v2(lines):
    digits_lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    total = 0
    for line in lines:
        for word, number in digits_lookup.items():
            line = line.replace(word, number)
        digits = [char for char in line if char.isdigit()]
        if digits:
            total += int(digits[0] + digits[-1])

    return total


def sum_calibration_values_v2_1(lines):
    digits_lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    total = 0
    for line in lines:
        for word in sorted(digits_lookup, key=len, reverse=True):
            line = line.replace(word, digits_lookup[word])
        digits = [char for char in line if char.isdigit()]
        print(line, digits)
        if digits:
            total += int(digits[0] + digits[-1])

    return total




def sum_calibration_values_v2_2(lines):
    digits_lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    total = 0
    for line in lines:
        words = re.findall(r'\b\w+\b', line)
        digits = [char for word in words for char in (digits_lookup[word] if word in digits_lookup else word) if
                  char.isdigit()]
        # print(line, digits)
        if digits:
            total += int(digits[0] + digits[-1])

    return total


def sum_calibration_values_v2_3(lines):
    digits_lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    total = 0
    for line in lines:
        i = 0
        new_line = ''
        while i < len(line):
            for word, num in digits_lookup.items():
                if line[i:i + len(word)] == word:
                    new_line += num
                    i += len(word)
                    break
            else:
                new_line += line[i]
                i += 1
        digits = [char for char in new_line if char.isdigit()]
        # print(line, digits)
        if digits:
            total += int(digits[0] + digits[-1])

    return total


def sum_calibration_values_v2_4(lines):
    digits_lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    total = 0
    for line in lines:
        i = 0
        new_line = ''
        while i < len(line):
            for word, num in digits_lookup.items():
                if line[i:i + len(word)] == word:
                    new_line += num
                    i += len(word)
                    break
            else:
                new_line += line[i]
                i += 1
        digits = [char for char in new_line if char.isdigit()]
        if len(digits) >= 2:
            print(line, digits)
            total += int(digits[0] + digits[-1])

    return total


def sum_calibration_values_v2_final(lines):
    digits_lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    total = 0
    for line in lines:
        i = 0
        new_line = ''
        while i < len(line):
            for word, num in digits_lookup.items():
                if line[i:i + len(word)] == word:
                    new_line += num
                    break
            else:
                new_line += line[i]
            i += 1
        digits = [char for char in new_line if char.isdigit()]
        if digits:
            total += int(digits[0] + digits[-1])

    return total


def sum_calibration_values_vx(lines):
    digits_lookup = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                     'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    total = 0
    for line in lines:
        i = 0
        new_line = ''
        while i < len(line):
            for word, num in digits_lookup.items():
                if line[i:i + len(word)] == word:
                    new_line += num
                    i += 1
                    break
            else:
                new_line += line[i]
                i += 1
        digits = [char for char in new_line if char.isdigit()]
        if digits:
            print(line, digits)
            total += int(digits[0] + digits[-1])

    return total


def test1():
    print("Test")
    lines = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split('\n')
    result = sum_calibration_values(lines)
    print("Part 1", 142 == result)

    lines = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split('\n')
    result = sum_calibration_values_v2(lines)
    print("Part 2", 281 == result)
    result = sum_calibration_values_v2_1(lines)
    print("Part 2", 281 == result)
    result = sum_calibration_values_v2_2(lines)
    print("Part 2", 281 == result)
    result = sum_calibration_values_v2_3(lines)
    print("Part 2", 281 == result)
    result = sum_calibration_values_v2_4(lines)
    print("Part 2", 281 == result)
    result = sum_calibration_values_v2_final(lines)
    print("Part 2", 281 == result)


def main():
    print("Main")
    with open('aoc2023_day01.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    print("Part 1", sum_calibration_values(lines))
    print("Part 2", sum_calibration_values_v2_final(lines))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
