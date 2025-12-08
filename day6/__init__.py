import itertools
import math
import re


def part_1_answer(lines):
    lines = [re.split(" +", line.strip()) for line in lines]
    problems = [list(problem) for problem in zip(*lines)]
    return sum(solve_part_1(problem) for problem in problems)


def solve_part_1(problem):
    op = problem[-1]
    numbers = [int(n) for n in problem[:-1]]
    return solve(numbers, op)


def solve(numbers, op):
    if op == "+":
        return sum(numbers)
    if op == "*":
        return math.prod(numbers)
    return None


def part_2_answer(lines):
    start_columns = [i for i, c in enumerate(lines[-1]) if c != " "]
    start_columns.append(len(lines[-1]) + 1)

    return sum(solve_part_2(lines, left, right)
               for left, right in itertools.pairwise(start_columns))


def solve_part_2(lines, left, right):
    problem = [line[left:right - 1] for line in lines]
    op = problem[-1][0]
    number_chars = problem[:-1]
    rotated_chars = list(reversed(["".join(column) for column in zip(*number_chars)]))
    numbers = [int(n.strip()) for n in rotated_chars]
    return solve(numbers, op)
