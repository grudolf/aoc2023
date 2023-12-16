import logging
from collections import deque

DIRECTION = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

REFLECT_SLASH = {
    # /
    'U': 'R',
    'D': 'L',
    'L': 'D',
    'R': 'U'
}

REFLECT_BACKSLASH = {
    # \
    'U': 'L',
    'D': 'R',
    'L': 'U',
    'R': 'D'
}


class Beam:
    def __init__(self, row: int, col: int, direction: chr):
        self.row = row
        self.col = col
        self.direction = direction

    def __str__(self):
        return f"({self.row}, {self.col}) {self.direction}"


class Tile:
    def __init__(self, type: str):
        self.type = type
        self.beam_hit = set()


class Cave:
    def __init__(self, lines: list[str]):
        self.rows = []
        for line in lines:
            self.rows.append([Tile(c) for c in line])
        self.width = len(self.rows)
        self.height = len(self.rows[0])

    def __str__(self):
        return '\n'.join([''.join([c.type for c in r]) for r in self.rows])

    def energized_map(self):
        return '\n'.join([''.join(['#' if c.beam_hit else ' ' for c in r]) for r in self.rows])

    def energized_count(self):
        return sum([len([c for c in r if c.beam_hit]) for r in self.rows])

    def shoot_beam(self, row: int, col: int, direction: chr):
        beams = deque([Beam(row, col, direction)])
        while len(beams):
            logging.debug("%d beams left", len(beams))
            beam = beams.popleft()
            while True:
                logging.debug('Beam %s', beam)
                tile = self.rows[beam.row][beam.col]
                if beam.direction in tile.beam_hit:
                    # tile already hit by beam and same direction
                    break
                tile.beam_hit = beam.direction

                if tile.type == '|':
                    if beam.direction in ['L', 'R']:
                        beam.direction = 'U'
                        beams.append(Beam(beam.row, beam.col, 'D'))
                elif tile.type == '-':
                    if beam.direction in ['U', 'D']:
                        beam.direction = 'L'
                        beams.append(Beam(beam.row, beam.col, 'R'))
                elif tile.type == '/':
                    beam.direction = REFLECT_SLASH[beam.direction]
                elif tile.type == '\\':
                    beam.direction = REFLECT_BACKSLASH[beam.direction]

                new_row, new_col = self.move(beam)
                if new_row is None:
                    break
                beam.row = new_row
                beam.col = new_col

    def move(self, beam):
        row = beam.row + DIRECTION[beam.direction][0]
        col = beam.col + DIRECTION[beam.direction][1]
        if 0 <= row < self.width and 0 <= col < self.height:
            return row, col
        return None, None

    def reset(self):
        for r in self.rows:
            for tile in r:
                tile.beam_hit = set()


def parse_input(lines):
    return [list(l) for l in lines]


def step1(cave):
    cave.shoot_beam(0, 0, 'R')
    print(cave)
    print(cave.energized_map())
    return cave.energized_count()


def step2(cave):
    best_result = 0
    configs = []
    configs.extend([0, c, 'D', 0] for c in range(cave.width))
    configs.extend([cave.height - 1, c, 'U', 0] for c in range(cave.width))
    configs.extend([r, 0, 'R', 0] for r in range(cave.height))
    configs.extend([r, cave.width - 1, 'L', 0] for r in range(cave.width))
    print(len(configs))
    for config in configs:
        row, col, direction, score = config
        cave.reset()
        cave.shoot_beam(row, col, direction)
        result = cave.energized_count()
        config[3] = result
        logging.info("Shoot from (%d, %d) %s: %d", row, col, direction, result)
        best_result = max(best_result, result)
    return best_result


def test1():
    lines = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....""".split('\n')
    cave = Cave(lines)
    print("Test1: ", 46 == step1(cave))
    print("Test1: ", 51 == step2(cave))


def main():
    with open('aoc2023_day16.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    cave = Cave(lines)
    print("Step1: ", step1(cave))
    print("Step2: ", step2(cave))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test1()
    main()
