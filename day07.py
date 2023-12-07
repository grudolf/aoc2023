import logging


def parse_input(lines):
    result = []
    for line in lines:
        hand = line.split()[0]
        bid = int(line.split()[1])
        result.append((hand, bid))
    return result


def rank_game(played_hand: str, step2):
    best_score = 0
    hands = [played_hand]
    if step2:
        # hands: played hand + hands with 'J' replaced for each used letter
        card_order = 'AKQT98765432J'
        if 'J' in played_hand:
            [hands.append(played_hand.replace('J', c)) for c in set(played_hand) if c != 'J']
            logging.debug(hands)
    else:
        card_order = 'AKQJT98765432'
    cards_dict = {}
    for i, c in enumerate(reversed(card_order), 1):
        # card, score, use_count
        cards_dict[c] = [c, i, 0]
    card_scores = [cards_dict[s[0]][1] for s in played_hand]
    for hand in hands:
        # reset and refill use_count
        for c in cards_dict.values():
            c[2] = 0
        for c in hand:
            cards_dict[c][2] += 1
        cards = sorted(cards_dict.values(), key=lambda x: (x[2], x[1]), reverse=True)
        # 5 + 0, 4 + 1, 3 + 2, 3 + 1, 2 + 2, 2 + 1, 1 + 1
        # 5*2 + 0 = 10, 4*2+1 = 9, 3*2+2 = 8, 2*2+2 = 6, 2*2+1 = 5, 1*2+1 = 3
        # 10, 9, 8, 6, 5, 3
        score = cards[0][2] * 2 + cards[1][2] if cards[0][2] > 1 else 0
        if score > best_score:
            best_score = score
    return best_score, card_scores


def rank_games(games, step2) -> int:
    ranked = []
    for hand, bid in games:
        score, card_scores = rank_game(hand, step2)
        ranked.append([hand, bid, score, card_scores])
    ranked = sorted(ranked, key=lambda x: (x[2], x[3]))
    total = 0
    for i, game in enumerate(ranked, 1):
        logging.debug("%s %s %s", i, game, i * game[1])
        total += i * game[1]
    return total


def test1():
    lines = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split('\n')
    result = rank_games(parse_input(lines), False)
    print("Part 1", 6440 == result)
    result = rank_games(parse_input(lines), True)
    print("Part 2", 5905 == result)


def main():
    with open('aoc2023_day07.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    result = rank_games(parse_input(lines), False)
    print("Part 1", result)
    result = rank_games(parse_input(lines), True)
    print("Part 2", result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
