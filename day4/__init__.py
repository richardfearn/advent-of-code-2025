def part_1_answer(grid):
    width, height = len(grid[0]), len(grid)
    return len(find_accessible(grid, width, height))


def find_accessible(grid, width, height):
    accessible = set()
    for y in range(height):
        for x in range(width):
            if grid[y][x] == "@":
                if count_neighbours(grid, width, height, x, y) < 4:
                    accessible.add((x, y))
    return accessible


def count_neighbours(grid, width, height, x, y):
    count = 0
    for nx in range(x - 1, x + 2):
        for ny in range(y - 1, y + 2):
            if (0 <= nx < width) and (0 <= ny < height) and ((x, y) != (nx, ny)):
                if grid[ny][nx] == "@":
                    count += 1
    return count


def part_2_answer(lines):
    grid: list[list[str]] = [list(row) for row in lines]
    width, height = len(grid[0]), len(grid)
    total_removed = 0
    while True:
        accessible = find_accessible(grid, width, height)
        if len(accessible) == 0:
            break
        for x, y in accessible:
            grid[y][x] = "."
        total_removed += len(accessible)
    return total_removed
