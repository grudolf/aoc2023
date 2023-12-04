import logging


def part1(games: list[tuple[int, set, set]]) -> int:
    total = 0
    for game in games:
        my_wins = game[1].intersection(game[2])
        if len(my_wins):
            score = 2 ** (len(my_wins) - 1)
            logging.debug((game[1], game[2], my_wins, score))
            total += score
    return total


def part2(games: list[tuple[int, set, set]]) -> int:
    """
    Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
    Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
    Your copy of card 2 also wins one copy each of cards 3 and 4.
    Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
    Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
    Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
    Your one instance of card 6 (one original) has no matching numbers and wins no more cards.

    Once all of the originals and copies have been processed,
    you end up with 1 instance of card 1,
    2 instances of card 2,
    4 instances of card 3,
    8 instances of card 4,
    14 instances of card 5,
    and 1 instance of card 6. In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!
    """
    logging.debug("Part2")
    won_cards = [0] * len(games)
    total = 0
    for index, game in enumerate(games):
        my_wins = len(game[1].intersection(game[2]))
        won_cards[index] += 1  # got this card anyway
        if my_wins:
            logging.debug("Card %s has %s matches, now %s copies owned", index + 1, my_wins, won_cards[index])
            for i in range(index + 1, index + my_wins + 1):
                logging.debug("Card %s, increasing copies from %s to %s", i+1, won_cards[i], won_cards[i] + won_cards[index])
                won_cards[i] += won_cards[index]
        total += won_cards[index]
        logging.debug("Card %s: copies %s, total cards %s", index + 1, won_cards[index], total)
    return total


def parse_input(lines) -> list[tuple[int, set, set]]:
    games = []
    for line in lines:
        game_data, lr = line.split(':')
        game_index = int(game_data[5:])
        winning = set(lr.split('|')[0].split())
        my = set(lr.split('|')[1].split())
        games.append((game_index, winning, my))
    return games


def test1():
    print('Test')
    lines = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split('\n')
    games = parse_input(lines)
    result = part1(games)
    print("Part 1", 13 == result)
    result = part2(games)
    print("Part 2", 30 == result)


def main():
    print('Main')
    with open('aoc2023_day04.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    games = parse_input(lines)
    result = part1(games)
    print("Part 1", result)
    result = part2(games)
    print("Part 2", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test1()
    main()
