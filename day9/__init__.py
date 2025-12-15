from collections import namedtuple
from itertools import combinations, pairwise

Point = namedtuple("Point", ["x", "y"])
Rectangle = namedtuple("Rectangle", ["top_left", "bottom_right"])


def part_1_answer(lines):
    red_tiles = parse(lines)
    return max(area(r) for r in all_possible_rectangles(red_tiles))


def all_possible_rectangles(red_tiles):
    for a, b in combinations(red_tiles, 2):
        yield make_rectangle(a, b)


def make_rectangle(a, b):
    x1, x2 = sorted((a.x, b.x))
    y1, y2 = sorted((a.y, b.y))
    return Rectangle(top_left=Point(x1, y1), bottom_right=Point(x2, y2))


def area(rect):
    width = abs(rect.bottom_right.x - rect.top_left.x) + 1
    height = abs(rect.bottom_right.y - rect.top_left.y) + 1
    return width * height


def part_2_answer(lines):
    red_tiles = parse(lines)
    lines = set(make_rectangle(a, b) for a, b in pairwise_circle(red_tiles))
    return max(area(r) for r in all_possible_rectangles(red_tiles) if no_overlaps(r, lines))


def pairwise_circle(items):
    # Given A, B, C, D:
    yield from pairwise(items)  # yields AB, BC, CD
    yield items[-1], items[0]  # yields DA


def no_overlaps(rect, lines):
    return not any(rectangles_overlap(rect, line) for line in lines)


def rectangles_overlap(r1, r2):
    if (r1.bottom_right.y <= r2.top_left.y) or (r2.bottom_right.y <= r1.top_left.y):
        return False
    if (r1.bottom_right.x <= r2.top_left.x) or (r2.bottom_right.x <= r1.top_left.x):
        return False
    return True


def parse(lines):
    return [Point(*(int(n) for n in pos.split(","))) for pos in lines]
