import operator
from collections import deque, defaultdict, namedtuple
from functools import reduce
from heapq import heappop, heappush

import z3
from z3 import Optimize

Machine = namedtuple("Machine", ["light_diagram", "wiring_schematics", "joltage_requirements"])


def part_1_answer(lines):
    manual = parse(lines)
    return sum(min_presses_for_lights(machine) for machine in manual)


def min_presses_for_lights(machine):
    edges = defaultdict(set)
    start = "." * len(machine.light_diagram)
    seen = set(start)
    to_explore = deque([start])

    while len(to_explore) > 0:
        current_state = to_explore.popleft()
        for schematic in machine.wiring_schematics:
            new_state = make_new_state(current_state, schematic)
            if new_state not in seen:
                seen.add(new_state)
                to_explore.append(new_state)
                edges[current_state].add(new_state)
                edges[new_state].add(current_state)

    dists = shortest_path(start, edges)
    return dists[machine.light_diagram]


def make_new_state(current_state, schematic):
    current_state = list(current_state)
    for i in schematic:
        current_state[i] = "." if (current_state[i] == "#") else "#"
    return "".join(current_state)


def shortest_path(start, edges):
    dist = {start: 0}
    q = [(0, start)]

    while len(q) > 0:
        u = heappop(q)[1]
        for v in edges[u]:
            alt = dist[u] + 1
            if (v not in dist) or (alt < dist[v]):
                dist[v] = alt
                heappush(q, (alt, v))

    return dist


def part_2_answer(lines):
    manual = parse(lines)
    return sum(min_presses_for_joltages(machine) for machine in manual)


def min_presses_for_joltages(machine):
    num_lights = len(machine.light_diagram)
    num_buttons = len(machine.wiring_schematics)

    # https://www.tautvidas.com/blog/2020/04/overcomplicating-meal-planning-with-z3-constraint-solver/

    opt = Optimize()

    presses = [z3.Int(f"p{i}") for i in range(num_buttons)]

    for i in range(num_lights):
        buttons = [b for j, b in enumerate(presses) if i in machine.wiring_schematics[j]]
        buttons_sum = reduce(operator.add, buttons)
        opt.add(buttons_sum == machine.joltage_requirements[i])

    for i in range(num_buttons):
        opt.add(presses[i] >= 0)

    total_presses = reduce(operator.add, presses)

    opt.minimize(total_presses)
    opt.check()
    m = opt.model()
    return sum(m[p].as_long() for p in presses)


def parse(lines):
    return [parse_machine(line) for line in lines]


def parse_machine(line):
    parts = line.split(" ")
    light_diagram = parts[0][1:-1]
    wiring_schematics = parts[1:-1]
    wiring_schematics = [{int(n) for n in s[1:-1].split(",")} for s in wiring_schematics]
    joltage_requirements = [int(n) for n in parts[-1][1:-1].split(",")]
    return Machine(light_diagram, wiring_schematics, joltage_requirements)
