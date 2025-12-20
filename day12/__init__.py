import utils


def part_1_answer(lines):
    presents, regions = parse(lines)
    occupied_spaces = [("".join(p)).count("#") for p in presents]
    return sum(region_can_fit_presents(region, occupied_spaces) for region in regions)


def region_can_fit_presents(region, occupied_spaces):
    area, counts = region
    width, height = area
    num_presents = len(counts)

    # are there more total occupied spaces than there are available in the region?
    total_region_spaces = width * height
    total_occupied_spaces = sum(occupied_spaces[i] * counts[i] for i in range(num_presents))
    if total_occupied_spaces > total_region_spaces:
        return False

    # can the presents just be placed next to each other without fitting them together?
    total_presents = sum(counts)
    total_3_by_3_spaces = (width // 3) * (height // 3)
    if total_presents <= total_3_by_3_spaces:
        return True

    raise NotImplementedError()


def parse(lines):
    groups = utils.group_lines(lines)
    presents = groups[:-1]
    presents = [p[1:] for p in presents]
    regions = groups[-1]
    regions = [parse_region(region) for region in regions]
    return presents, regions


def parse_region(region):
    area, counts = region.split(": ")
    area = tuple(int(n) for n in area.split("x"))
    counts = [int(n) for n in counts.split(" ")]
    return area, counts
