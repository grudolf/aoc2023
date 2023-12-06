import logging


def race(times: list[int], distances: list[int]):
    total_wins = 1
    for max_time, record_distance in zip(times, distances):
        logging.debug("Max time %s, record distance %s", max_time, record_distance)
        wins = 0
        for time in range(max_time):
            speed = time
            distance = (max_time - time) * speed
            if win := distance > record_distance:
                wins += 1
            # logging.debug(" time %s, distance %s, win: %s", time, distance, win)
        logging.debug("%s of %s races win", wins, max_time)
        total_wins = total_wins * wins
    return total_wins


def parse_input(lines):
    times = [int(i) for i in lines[0].split(':')[1].split()]
    distances = [int(i) for i in lines[1].split(':')[1].split()]
    return times, distances


def parse_input2(lines):
    times = [i for i in lines[0].split(':')[1].split()]
    distances = [i for i in lines[1].split(':')[1].split()]
    return [int(''.join(times))], [int(''.join(distances))]


def test1():
    lines = """Time:      7  15   30
Distance:  9  40  200""".split('\n')
    times, distances = parse_input(lines)
    result = race(times, distances)
    print("Part 1", 288 == result)

    times, distances = parse_input2(lines)
    result = race(times, distances)
    print("Part 2", 71503 == result)


def main():
    with open('aoc2023_day06.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    times, distances = parse_input(lines)
    result = race(times, distances)
    print("Part 1", result)

    times, distances = parse_input2(lines)
    result = race(times, distances)
    print("Part 2", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
