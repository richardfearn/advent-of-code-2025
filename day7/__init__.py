from functools import cache


def part_1_answer(diagram):
    beam_positions = {diagram[0].index("S")}
    num_splits = 0

    for row in diagram[1:]:
        splitter_positions = {x for x, c in enumerate(row) if c == "^"}
        stop_positions = beam_positions & splitter_positions
        num_splits += len(stop_positions)
        for i in stop_positions:
            beam_positions -= {i}
            beam_positions |= {i - 1, i + 1}

    return num_splits


def part_2_answer(diagram):
    start_pos = diagram[0].index("S")
    height = len(diagram)
    splitters = find_splitters(diagram)

    @cache
    def num_timelines(x, y):
        if y == (height - 1):
            return 1

        y += 1
        if (x, y) in splitters:
            return num_timelines(x - 1, y) + num_timelines(x + 1, y)
        return num_timelines(x, y)

    return num_timelines(start_pos, 0)


def find_splitters(diagram):
    splitters = set()
    for y, row in enumerate(diagram):
        for x, c in enumerate(row):
            if c == "^":
                splitters.add((x, y))
    return splitters
