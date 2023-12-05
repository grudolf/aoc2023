import logging


def part1(seeds: list[int], maps: list[list[int, int, int]]) -> int:
    lowest_location = 0
    for seed in seeds:
        logging.debug("Mapping %s", seed)
        mapped = seed
        for m in maps:
            logging.debug(m)
            for e in m:
                if e[1] <= mapped < e[1] + e[2]:
                    new = mapped + e[0] - e[1]
                    logging.debug(" Mapped from %s to %s", mapped, new)
                    mapped = new
                    break
        if lowest_location == 0 or mapped < lowest_location:
            lowest_location = mapped
        logging.info("Mapped seed %s to location %s, lowest is %s", seed, mapped, lowest_location)

    return lowest_location


def part2(seeds: list[int], maps: list[list[int, int, int]]) -> int:
    lowest_location = 0
    for seed, rng in zip(seeds[0::2], seeds[1::2]):
        logging.info("Working on %s -(%s)- %s", seed, rng, seed + rng)

        current_seed = seed
        while current_seed <= seed + rng:
            # attempt to skip to end
            skip = max(1, seed + rng - current_seed)
            mapped = current_seed
            for m in maps:
                # logging.debug(m)
                for e in m:
                    if e[1] <= mapped < e[1] + e[2]:
                        # shorten skip if needed
                        max_skip = e[1] + e[2] - mapped
                        if max_skip < skip and skip != 1:
                            if max_skip < 1:
                                max_skip = 1
                            logging.debug(" Seed %s, shorten skip from %s to %s", current_seed, skip, max_skip)
                            skip = max_skip
                        new = mapped + e[0] - e[1]
                        mapped = new
                        break
            if lowest_location == 0 or mapped < lowest_location:
                lowest_location = mapped
            logging.info(" Mapped seed %s to location %s, lowest is %s", current_seed, mapped, lowest_location)
            current_seed += skip
    return lowest_location


def parse_input(lines) -> (list, list):
    seeds = [int(s) for s in lines[0].split(':')[1].split()]
    maps = []
    map = []
    for line in lines[1:]:
        s = line.split()
        if len(s) == 3 and s[0][0].isdigit():
            map.append([int(s[0]), int(s[1]), int(s[2])])
        else:
            if len(map):
                maps.append(map)
                map = []
    if len(map):
        maps.append(map)
    logging.debug(seeds)
    logging.debug(maps)
    return seeds, maps


def test1():
    print('Test')
    lines = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split('\n')
    seeds, maps = parse_input(lines)
    result = part1(seeds, maps)
    print("Part 1", 35 == result)
    result = part2(seeds, maps)
    print("Part 2", 46 == result)


def main():
    print('Main')
    with open('aoc2023_day05.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    seeds, maps = parse_input(lines)
    result = part1(seeds, maps)
    print("Part 1", result)
    result = part2(seeds, maps)
    print("Part 2", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
