import heapq
import logging

DIRECTION = {
    #    N
    #   W E
    #    S
    #
    'N': (-1, 0),
    'S': (1, 0),
    'W': (0, -1),
    'E': (0, 1),
}

TURN = {
    # current direction: turn left, turn right
    'N': ('W', 'E'),
    'S': ('E', 'W'),
    'E': ('S', 'N'),
    'W': ('N', 'S')

}


class Block:
    def __init__(self, row: int, col: int, heat_loss: chr):
        self.row = row
        self.col = col
        self.heat_loss = int(heat_loss)

    def __str__(self):
        return f"({self.row}, {self.col}) {self.heat_loss}"


class Grid:
    def __init__(self, lines: list[str]):
        self.rows = []
        for r, line in enumerate(lines):
            self.rows.append([Block(r, c, h) for c, h in enumerate(line)])
        self.width = len(self.rows)
        self.height = len(self.rows[0])

    def __str__(self):
        return '\n'.join([''.join([str(c.heat_loss) for c in r]) for r in self.rows])

    def calculate_heat_loss2(self, min_steps: int, max_steps: int):
        q = []
        heapq.heappush(q, (0, 0, 0, 'E'))
        heapq.heappush(q, (0, 0, 0, 'S'))
        scores = dict()
        visited = set()
        logging.info("Dimension %d x %d", self.height, self.width)
        i = 0
        while q:
            i += 1
            score, r, c, direction = heapq.heappop(q)

            prev_best_score = scores.get((r, c, direction), 1000000)
            if prev_best_score < score:
                continue
            # better score found
            scores[(r, c, direction)] = score
            # logging.debug((str(self.rows[r][c]), direction, score))

            for new_direction in TURN[direction]:
                nr, nc = r, c
                dr, dc = DIRECTION[direction]
                new_score = score
                for s in range(1, max_steps + 1):
                    nr += dr
                    nc += dc
                    if 0 <= nr < self.height and 0 <= nc < self.width:
                        new_score += self.rows[nr][nc].heat_loss
                        if s >= min_steps and (nr, nc, new_direction, s) not in visited:
                            visited.add((nr, nc, new_direction, s))
                            heapq.heappush(q, (new_score, nr, nc, new_direction))

        result = [scores[(self.height - 1, self.width - 1, d)] for d in DIRECTION.keys()]
        logging.info("Ended after %d iterations, result: %s", i, result)
        return min(result)


def parse_input(lines):
    return [list(l) for l in lines]


def test1():
    lines = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".split('\n')
    city = Grid(lines)
    print("Test 1A: ", 102 == city.calculate_heat_loss2(1, 3))
    print("Test 2A: ", 94 == city.calculate_heat_loss2(4, 10))


def main():
    with open('aoc2023_day17.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    city = Grid(lines)
    print("Step 1A: ", city.calculate_heat_loss2(1, 3))
    print("Step 2: ", city.calculate_heat_loss2(4, 10))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
