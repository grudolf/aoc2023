import logging
import re
# dicts don't exist
# from collections import OrderedDict


def parse_input(lines):
    return [list(l) for l in lines]


def hashed(seq):
    current_value = 0
    for char in seq:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def step1(init_sequence):
    results = [hashed(seq) for seq in init_sequence]
    return sum(results)


def step2(init_sequence):
    # dicts don't exist
    # boxes = [OrderedDict() for _ in range(256)]
    boxes = [[] for _ in range(256)]
    for seq in init_sequence:
        label, op, param = re.findall("^([a-z]+)([-=])(.*)$", seq)[0]
        logging.debug((label, op, param))
        box = boxes[hashed(label)]
        if op == '=':
            # dicts don't exist
            # box[label] = param
            found = False
            for entry in box:
                if entry[0] == label:
                    entry[1] = param
                    found = True
                    break
            if not found:
                box.append([label, param])
        elif op == '-':
            for entry in box:
                if entry[0] == label:
                    del box[box.index(entry)]
                    break

    power = 0
    for i in range(256):
        if len(boxes[i]):
            logging.debug((i, boxes[i]))
            for j, item in enumerate(boxes[i]):
                item_power = (i + 1) * (j + 1) * int(item[1])
                power += item_power
                logging.info((j, item, item_power, power))
    return power


def test1():
    print(52 == hashed('HASH'))
    init_sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(',')
    print("Test1: ", 1320 == step1(init_sequence))
    print("Test2: ", 145 == step2(init_sequence))


def main():
    with open('aoc2023_day15.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    print('Step 1')
    for line in lines:
        init_sequence = line.split(',')
        print(line)
        print("Step 1: ", step1(init_sequence))
        print("Step 2: ", step2(init_sequence))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test1()
    main()
