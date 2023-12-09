import logging
import re
from collections import OrderedDict
from itertools import cycle
from math import lcm


def parse_input(lines):
    instructions = [i for i in lines[0]]

    r = "^([A-Z0-9]*) = \(([A-Z0-9]*), ([A-Z0-9]*).*"
    nodes = OrderedDict()
    for line in lines[2:]:
        node, left, right = re.findall(r, line)[0]
        nodes[node] = (left, right)
    return instructions, nodes


def walk(instructions, nodes):
    loc = 'AAA'
    end = 'ZZZ'
    step = 0
    for instruction in cycle(instructions):
        node = nodes[loc]
        step += 1
        next_location = node[0] if instruction == 'L' else node[1]
        if step < 20 or step % 1000 == 0:
            logging.debug("%s: %s %s, going %s to %s", step, loc, node, instruction, next_location)
        if next_location == end:
            break
        loc = next_location
    return step


def fly(instructions, nodes):
    starting_locations = [l for l in nodes.keys() if l.endswith('A')]
    logging.info("Starting locations: %s", starting_locations)
    cycle_lengths = []
    for starting_location in starting_locations:
        logging.info(starting_location)
        loc = starting_location
        step = 0
        zzzs = {}
        for instruction in cycle(instructions):
            node = nodes[loc]
            step += 1
            next_location = node[0] if instruction == 'L' else node[1]
            #logging.debug("%s: %s %s, going %s to %s", step, loc, node, instruction, next_location)
            if next_location == starting_location or next_location in zzzs:
                logging.info("Loop detected at location: %s", next_location)
                break
            if next_location.endswith('Z'):
                logging.debug("Found %s at step %s", next_location, step)
                zzzs[next_location] = step
            loc = next_location
        if len(zzzs) == 0:
            raise ValueError(f"Cannot reach XXZ from {starting_location}")
        if len(zzzs) > 1:
            # we're not ready
            raise ValueError("Multiple XXZ locations found")
        v = list(zzzs.values())[0]
        cycle_lengths.append(v)

    for loc, v in zip(starting_locations, cycle_lengths):
        logging.info("%s : %s", loc, v)
    result = lcm(*cycle_lengths)
    logging.info("LCM : %s", result)
    return result


def test1():
    lines = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split('\n')
    instructions, nodes = parse_input(lines)
    print(2 == walk(instructions, nodes))

    lines = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".split('\n')
    instructions, nodes = parse_input(lines)
    print(6 == walk(instructions, nodes))


def test2():
    lines = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split('\n')
    instructions, nodes = parse_input(lines)
    print(6 == fly(instructions, nodes))


def main():
    with open('aoc2023_day08.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    instructions, nodes = parse_input(lines)
    print("Part 1", walk(instructions, nodes))
    print("Part 2", fly(instructions, nodes))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    test2()
    main()
