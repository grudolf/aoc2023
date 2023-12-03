import logging


def part1(games: list[tuple[int, list[dict[str, int]]]], red: int, green: int, blue: int) -> int:
    score = 0
    for game_index, subset in games:
        valid = True
        for subset_data in subset:
            red_count = subset_data.get('red', 0)
            green_count = subset_data.get('green', 0)
            blue_count = subset_data.get('blue', 0)
            if red_count > red or green_count > green or blue_count > blue:
                valid = False
                break
        if valid:
            score += game_index
            logging.debug("Index: %s, score %s, subset: %s", game_index, score, subset)
    return score


def part2(games: list[tuple[int, list[dict[str, int]]]]) -> int:
    score = 0
    for game_index, subset in games:
        max_red = 0
        max_green = 0
        max_blue = 0
        for subset_data in subset:
            max_red = max(max_red, subset_data.get('red', 0))
            max_green = max(max_green, subset_data.get('green', 0))
            max_blue = max(max_blue, subset_data.get('blue', 0))
        power = max_red * max_green * max_blue
        score += power
        logging.debug("Index: %s, power: %s, score: %s", game_index, power, score)
    return score


def parse_input(lines) -> list[tuple[int, list[dict[str, int]]]]:
    games = []
    for line in lines:
        game_data, subsets_data = line.split(':')  # "Game ?", " 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        game_index = int(game_data[5:])
        subsets = []
        for subset_data in subsets_data.split(';'):
            scores = {}
            # " 3 blue, 4 red"
            for score_data in subset_data.split(','):
                count, color = score_data.split()
                scores[color] = int(count)
            subsets.append(scores)
        games.append((game_index, subsets))
    return games


def test1():
    print('Test')
    lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split('\n')
    games = parse_input(lines)
    result = part1(games, 12, 13, 14)
    print("Part 1", 8 == result)

    lines = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split('\n')
    games = parse_input(lines)
    result = part2(games)
    print("Part 2", 2286 == result)


def main():
    print('Main')
    with open('aoc2023_day02.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    games = parse_input(lines)
    result = part1(games, 12, 13, 14)
    print("Part 1", result)
    result = part2(games)
    print("Part 2", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
