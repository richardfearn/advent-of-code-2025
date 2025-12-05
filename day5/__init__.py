import itertools

import utils


def part_1_answer(database):
    fresh_ranges, ingredients = parse(database)
    return sum(is_fresh(ingredient, fresh_ranges) for ingredient in ingredients)


def is_fresh(ingredient, fresh_ranges):
    return any(ingredient in r for r in fresh_ranges)


def part_2_answer(database):
    fresh_ranges, _ = parse(database)

    boundaries = set()
    for r in fresh_ranges:
        boundaries |= {r.start, r.stop}

    num_fresh_ingredients = 0

    for start, stop in itertools.pairwise(sorted(boundaries)):
        if any(start in r for r in fresh_ranges):
            num_fresh_ingredients += (stop - start)

    return num_fresh_ingredients


def parse(database):
    fresh_ranges, ingredients = utils.group_lines(database)  # pylint: disable=unbalanced-tuple-unpacking
    fresh_ranges = [parse_range(r) for r in fresh_ranges]
    ingredients = [int(n) for n in ingredients]
    return fresh_ranges, ingredients


def parse_range(r):
    start, stop = r.split("-")
    return range(int(start), int(stop) + 1)
