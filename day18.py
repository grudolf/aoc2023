import logging

DIRECTION = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

TO_DIR = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U',
}


class Point:
    def __init__(self, direction: chr, len: int, row: int, col: int, color: str):
        self.direction = direction
        self.len = len
        self.row = row
        self.col = col
        self.color = color

    def __str__(self):
        return f"({self.row}, {self.col}) {self.direction} {self.len}"


class Dig:
    def __init__(self, lines: list[str], part2):
        self.points = []
        r, c = 0, 0
        min_r, min_c = 0, 0
        max_r, max_c = 0, 0
        for line in lines:
            d, l, color = line.split()
            if part2:
                l = int(color[2:-2], 16)
                d = TO_DIR[color[-2]]
            point = Point(d, int(l), r, c, color)
            direction = DIRECTION[d]
            r += direction[0] * int(l)
            c += direction[1] * int(l)
            self.points.append(point)
            min_r = min(min_r, r)
            min_c = min(min_c, c)
            max_r = max(max_r, r)
            max_c = max(max_c, c)
        logging.info((min_r, min_c, max_r, max_c))
        # relocation not needed
        # if min_r<0:
        #     for p in self.points:
        #         p.row = p.row - min_r
        #     max_r = max_r - min_r
        #     min_r -= min_r
        # if min_c<0:
        #     for p in self.points:
        #         p.col = p.col - min_c
        #     max_c = max_c - min_c
        #     min_c -= min_c
        #logging.info((min_r, min_c, max_r, max_c))

        # self.width = len(self.points)
        # self.height = len(self.points[0])

    def __str__(self):
        return '\n'.join([''.join([c.type for c in r]) for r in self.points])

    def area(self):
        # shoelace formula - A = internal area, no borders, result too low without it
        n = len(self.points)
        a = 0.0
        boundary = 0  # perimeter
        for i in range(n):
            j = (i + 1) % n
            a += self.points[i].row * self.points[j].col
            a -= self.points[j].row * self.points[i].col
            boundary += self.points[i].len
        a = abs(a) / 2.0
        # Pick theorem: i + b/2 - 1 = A (i = internal points, b = boundary points)
        # i = A - b/2 + 1
        # i + b = A + b/2 + 1
        return a + boundary/2 + 1, boundary


def parse_input(lines):
    return [list(l) for l in lines]


def test1():
    lines = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".split('\n')
    dig = Dig(lines, 0)
    #print('\n'.join([str(p) for p in dig.points]))
    area, boundary = dig.area()
    print("Test 1 area", area == 62, area)
    print("Test 1 boundary", boundary == 38, boundary)
    dig = Dig(lines, 1)
    #print('\n'.join([str(p) for p in dig.points]))
    area, boundary = dig.area()
    print("Test 2", area == 952408144115, area)


def main():
    with open('aoc2023_day18.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    dig = Dig(lines, 0)
    area, boundary = dig.area()
    print("Step 1", area)
    dig = Dig(lines, 1)
    area, boundary = dig.area()
    print("Step 2", area)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test1()
    main()
